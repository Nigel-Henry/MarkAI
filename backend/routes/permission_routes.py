from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

permission_routes = Blueprint('permission_routes', __name__)

@permission_routes.route('/api/permissions', methods=['POST'])
@jwt_required()
def create_permission():
    permission_name = request.json.get('permission_name')
    
    if not permission_name:
        return jsonify({"error": "Permission name is required"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO permissions (permission_name) VALUES (?)", (permission_name,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Permission created successfully!"})

@permission_routes.route('/api/permissions', methods=['GET'])
@jwt_required()
def get_permissions():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM permissions")
            permissions = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"permissions": permissions})