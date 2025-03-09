from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from bson import ObjectId
from datetime import timedelta
import math
from services.database import mongo

admin_bp = Blueprint('admin', __name__)

# Admin Authentication
@admin_bp.route('/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if data.get('username') == 'admin' and data.get('password') == 'Test@1234!Secure':
        access_token = create_access_token(identity='admin')
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid admin credentials"}), 401

# Player CRUD Operations
@admin_bp.route('/players', methods=['GET', 'POST'])
@jwt_required()
def manage_players():
    if get_jwt_identity() != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    if request.method == 'GET':
        players = list(mongo.db.players.find())
        return jsonify([{**player, '_id': str(player['_id'])} for player in players])
    
    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['Name', 'University', 'Category', 'Total_Runs', 
                         'Balls_Faced', 'Innings_Played', 'Wickets', 
                         'Overs_Bowled', 'Runs_Conceded']
        
        if not all(field in data for field in required_fields):
            return jsonify({"msg": "Missing required fields"}), 400
        
        result = mongo.db.players.insert_one(data)
        return jsonify({'_id': str(result.inserted_id)}), 201

@admin_bp.route('/players/<string:player_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def single_player_operations(player_id):
    if get_jwt_identity() != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    if request.method == 'PUT':
        data = request.get_json()
        result = mongo.db.players.update_one(
            {'_id': ObjectId(player_id)},
            {'$set': data}
        )
        if result.modified_count:
            return jsonify({"msg": "Player updated successfully"}), 200
        return jsonify({"msg": "Player not found"}), 404
    
    if request.method == 'DELETE':
        result = mongo.db.players.delete_one({'_id': ObjectId(player_id)})
        if result.deleted_count:
            return jsonify({"msg": "Player deleted successfully"}), 200
        return jsonify({"msg": "Player not found"}), 404

# Player Statistics
@admin_bp.route('/players/<string:player_id>/stats')
@jwt_required()
def player_stats(player_id):
    if get_jwt_identity() != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    if not player:
        return jsonify({"msg": "Player not found"}), 404

    # Batting calculations
    batting_sr = (player['Total_Runs'] / player['Balls_Faced']) * 100 if player['Balls_Faced'] else 0
    batting_avg = player['Total_Runs'] / player['Innings_Played'] if player['Innings_Played'] else 0
    
    # Bowling calculations
    balls_bowled = player['Overs_Bowled'] * 6 if player['Overs_Bowled'] else 0
    bowling_sr = balls_bowled / player['Wickets'] if player['Wickets'] else 0
    economy = (player['Runs_Conceded'] / balls_bowled) * 6 if balls_bowled else 0
    
    # Points and value calculations
    points = ((batting_sr / 5) + (batting_avg * 0.8)) + \
            ((500 / batting_sr if batting_sr else 0) + (140 / economy if economy else 0))
    value = round(((9 * points + 100) * 1000) / 50000) * 50000

    return jsonify({
        'batting_strike_rate': round(batting_sr, 2),
        'batting_average': round(batting_avg, 2),
        'bowling_strike_rate': round(bowling_sr, 2),
        'economy': round(economy, 2),
        'points': round(points, 2),
        'value': value,
        'player_details': {
            'Name': player['Name'],
            'University': player['University'],
            'Category': player['Category']
        }
    })

# Tournament Summary
@admin_bp.route('/tournament/summary')
@jwt_required()
def tournament_summary():
    if get_jwt_identity() != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    # Total runs and wickets
    pipeline = [{
        '$group': {
            '_id': None,
            'total_runs': {'$sum': '$Total_Runs'},
            'total_wickets': {'$sum': '$Wickets'}
        }
    }]
    summary = list(mongo.db.players.aggregate(pipeline))[0]

    # Highest run scorer
    top_scorer = mongo.db.players.find_one(
        sort=[("Total_Runs", -1)]
    )
    
    # Highest wicket taker
    top_wicket_taker = mongo.db.players.find_one(
        sort=[("Wickets", -1)]
    )

    return jsonify({
        'total_runs': summary['total_runs'],
        'total_wickets': summary['total_wickets'],
        'top_scorer': {
            'name': top_scorer['Name'],
            'runs': top_scorer['Total_Runs'],
            'university': top_scorer['University']
        },
        'top_wicket_taker': {
            'name': top_wicket_taker['Name'],
            'wickets': top_wicket_taker['Wickets'],
            'university': top_wicket_taker['University']
        }
    })

# Real-Time Updates WebSocket Handler
@admin_bp.route('/refresh', methods=['POST'])
@jwt_required()
def trigger_updates():
    if get_jwt_identity() != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    # Broadcast update to all connected clients
    from services.realtime import socketio
    socketio.emit('data_updated', {'message': 'Admin data changed'})
    return jsonify({"msg": "Update signal sent"}), 200