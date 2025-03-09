from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from bson import ObjectId
from datetime import timedelta
import math
from services.database import mongo
from services.realtime import socketio
from services.utils import calculate_player_value
from extensions import bcrypt, mongo, socketio

user_bp = Blueprint('user', __name__)

# User Authentication
@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400
    
    if mongo.db.users.find_one({"username": data['username']}):
        return jsonify({"msg": "Username already exists"}), 409
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user_data = {
        "username": data['username'],
        "password": hashed_password,  # In production, use password hashing
        "budget": 9000000,
        "team": [],
        "total_points": 0,
        "points_history": []
    }
    
    result = mongo.db.users.insert_one(user_data)
    return jsonify({
        "msg": "User created successfully",
        "user_id": str(result.inserted_id)
    }), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = mongo.db.users.find_one({"username": data.get('username')})

    if user and bcrypt.check_password_hash(user['password'], data.get('password')):
        access_token = create_access_token(identity=str(user['_id']))
        return jsonify({
            "access_token": access_token,
            "user_id": str(user['_id'])
        }), 200

    return jsonify({"msg": "Invalid credentials"}), 401
    

# Player Management
@user_bp.route('/players', methods=['GET'])
@jwt_required()
def get_all_players():
    players = list(mongo.db.players.find({}, {'points': 0}))
    return jsonify([{
        "_id": str(player["_id"]),
        "Name": player["Name"],
        "University": player["University"],
        "Category": player["Category"],
        "value": player.get("value", 0)
    } for player in players]), 200

@user_bp.route('/players/<string:category>', methods=['GET'])
@jwt_required()
def get_players_by_category(category):
    players = list(mongo.db.players.find(
        {"Category": category},
        {'points': 0}
    ))
    return jsonify([{
        "_id": str(player["_id"]),
        "Name": player["Name"],
        "University": player["University"],
        "value": player.get("value", 0)
    } for player in players]), 200

# Team Management
@user_bp.route('/team', methods=['GET'])
@jwt_required()
def get_user_team():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    team_details = []
    for player in user['team']:
        player_data = mongo.db.players.find_one(
            {"_id": ObjectId(player['player_id'])},
            {'points': 0}
        )
        if player_data:
            team_details.append({
                "player_id": str(player_data["_id"]),
                "Name": player_data["Name"],
                "University": player_data["University"],
                "value": player_data.get("value", 0)
            })
    
    return jsonify({
        "team": team_details,
        "budget": user["budget"],
        "team_size": len(team_details),
        "total_points": user["total_points"] if len(team_details) == 11 else 0
    }), 200

@user_bp.route('/team/add', methods=['POST'])
@jwt_required()
def add_player_to_team():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    player = mongo.db.players.find_one({"_id": ObjectId(data['player_id'])})
    
    if not user or not player:
        return jsonify({"msg": "User or player not found"}), 404
    
    if any(p['player_id'] == data['player_id'] for p in user['team']):
        return jsonify({"msg": "Player already in team"}), 400
    
    if user['budget'] < player.get('value', 0):
        return jsonify({"msg": "Insufficient budget"}), 400
    
    # Update user team and budget
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$push": {"team": {"player_id": str(player["_id"]), "value": player["value"]}},
            "$inc": {"budget": -player["value"]}
        }
    )
    
    # Calculate new total points if team is complete
    updated_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if len(updated_user['team']) == 11:
        total_points = sum(calculate_player_value(p['value']) for p in updated_user['team'])
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"total_points": total_points}}
        )
    
    socketio.emit('team_update', {'user_id': user_id})
    return jsonify({"msg": "Player added to team"}), 200

@user_bp.route('/team/remove/<string:player_id>', methods=['DELETE'])
@jwt_required()
def remove_player_from_team(player_id):
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    if not user:
        return jsonify({"msg": "User not found"}), 404
    
    player_to_remove = next((p for p in user['team'] if p['player_id'] == player_id), None)
    if not player_to_remove:
        return jsonify({"msg": "Player not in team"}), 404
    
    # Update user team and budget
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$pull": {"team": {"player_id": player_id}},
            "$inc": {"budget": player_to_remove['value']}
        }
    )
    
    # Reset points if team becomes incomplete
    if len(user['team']) == 11:
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"total_points": 0}}
        )
    
    socketio.emit('team_update', {'user_id': user_id})
    return jsonify({"msg": "Player removed from team"}), 200

# Leaderboard
@user_bp.route('/leaderboard', methods=['GET'])
@jwt_required()
def get_leaderboard():
    current_user_id = get_jwt_identity()
    users = list(mongo.db.users.find({}, {
        "username": 1,
        "total_points": 1,
        "_id": 1
    }))
    
    leaderboard = []
    for user in users:
        leaderboard.append({
            "username": user["username"],
            "points": user["total_points"],
            "is_current_user": str(user["_id"]) == current_user_id
        })
    
    # Sort by points descending
    leaderboard.sort(key=lambda x: x["points"], reverse=True)
    
    return jsonify(leaderboard), 200