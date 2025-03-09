from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import os

app = Flask(__name__)

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="spirit11_db"  # Replace with your database name
    )

# Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register User
@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    
    hashed_password = hash_password(password)

    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "User registered successfully!"}), 201

# Login User
@app.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    hashed_password = hash_password(password)

    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()

    if user:
        return jsonify({"message": "Login successful!", "user_id": user[0]}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Get All Players
@app.route("/players", methods=["GET"])
def get_players():
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(players), 200

# Select Players for a Team
@app.route("/select_player", methods=["POST"])
def select_player():
    data = request.get_json()
    user_id = data.get("user_id")
    player_id = data.get("player_id")
    
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT budget FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        budget = user[0]
        cursor.execute("SELECT value FROM players WHERE id = %s", (player_id,))
        player = cursor.fetchone()
        
        if player:
            player_value = player[0]
            if budget >= player_value:
                # Add player to the user's team
                cursor.execute("INSERT INTO teams (user_id, player_id) VALUES (%s, %s)", (user_id, player_id))
                # Deduct player's value from budget
                cursor.execute("UPDATE users SET budget = budget - %s WHERE id = %s", (player_value, user_id))
                connection.commit()
                
                cursor.close()
                connection.close()
                
                return jsonify({"message": "Player selected successfully!"}), 201
            else:
                return jsonify({"message": "Insufficient budget!"}), 400
        else:
            return jsonify({"message": "Player not found!"}), 404
    else:
        return jsonify({"message": "User not found!"}), 404

# Run the App
if __name__ == "__main__":
    app.run(debug=True)
