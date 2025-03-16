from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

admin_routes = Blueprint('admin_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

def is_admin(username):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user and user['role'] == 'admin'

@admin_routes.route('/api/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    username = get_jwt_identity()
    if is_admin(username):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id, username, role FROM users")
        users = c.fetchall()
        conn.close()
        return jsonify([dict(user) for user in users])
    return jsonify({"error": "Unauthorized!"}), 403

@admin_routes.route('/api/admin/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    username = get_jwt_identity()
    if is_admin(username):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "User deleted successfully!"})
    return jsonify({"error": "Unauthorized!"}), 403