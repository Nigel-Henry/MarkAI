from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

settings_routes = Blueprint('settings_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@settings_routes.route('/api/settings', methods=['POST'])
@jwt_required()
def update_settings():
    try:
        setting_name = request.json.get('setting_name')
        setting_value = request.json.get('setting_value')
        
        if not setting_name or not setting_value:
            return jsonify({"error": "Invalid input"}), 400

        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO settings (setting_name, setting_value) VALUES (?, ?)", 
                      (setting_name, setting_value))
            conn.commit()

        return jsonify({"message": "Settings updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@settings_routes.route('/api/settings', methods=['GET'])
@jwt_required()
def get_settings():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM settings")
            settings = c.fetchall()

        return jsonify({"settings": [dict(row) for row in settings]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500