from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

log_routes = Blueprint('log_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@log_routes.route('/api/logs', methods=['POST'])
@jwt_required()
def create_log():
    log_message = request.json.get('log_message')
    if not log_message:
        return jsonify({"error": "Log message is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO logs (log_message) VALUES (?)", (log_message,))
            conn.commit()
        return jsonify({"message": "Log created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@log_routes.route('/api/logs', methods=['GET'])
@jwt_required()
def get_logs():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM logs")
            logs = c.fetchall()
        return jsonify({"logs": [dict(log) for log in logs]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500