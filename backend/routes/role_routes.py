from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

role_routes = Blueprint('role_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@role_routes.route('/api/roles', methods=['POST'])
@jwt_required()
def create_role():
    role_name = request.json.get('role_name')
    if not role_name:
        return jsonify({"error": "Role name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO roles (role_name) VALUES (?)", (role_name,))
            conn.commit()
        return jsonify({"message": "Role created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@role_routes.route('/api/roles', methods=['GET'])
@jwt_required()
def get_roles():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM roles")
            roles = c.fetchall()
        return jsonify({"roles": [dict(role) for role in roles]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500