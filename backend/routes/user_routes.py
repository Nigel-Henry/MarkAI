from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/users', methods=['POST'])
@jwt_required()
def create_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400
        
        hashed_password = generate_password_hash(password)
        
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()

        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_routes.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT id, username FROM users")
            users = c.fetchall()

        return jsonify({"users": users}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500