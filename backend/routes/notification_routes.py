from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

notification_routes = Blueprint('notification_routes', __name__)

@notification_routes.route('/api/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    user_id = get_jwt_identity()
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM notifications WHERE user_id = ?", (user_id,))
            notifications = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"notifications": notifications})