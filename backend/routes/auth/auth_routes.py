from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import sqlite3

# Create a Blueprint for authentication routes
auth_routes = Blueprint('auth_routes', __name__)

# Register route
@auth_routes.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required!"}), 400
    
    hashed_password = generate_password_hash(password)
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Login route
@auth_routes.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required!"}), 400
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = c.fetchone()
        
        if user and check_password_hash(user[2], password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid credentials!"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Protected route (for testing JWT)
@auth_routes.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Add points route
@auth_routes.route('/api/add_points', methods=['POST'])
@jwt_required()
def add_points():
    username = get_jwt_identity()
    points = request.json.get('points')
    
    if not points or not isinstance(points, int):
        return jsonify({"error": "Points must be an integer!"}), 400
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE users SET points = points + ? WHERE username = ?", (points, username))
            conn.commit()
        return jsonify({"message": "Points added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
