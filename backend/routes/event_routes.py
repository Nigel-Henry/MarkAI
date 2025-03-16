from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

event_routes = Blueprint('event_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@event_routes.route('/api/events', methods=['POST'])
@jwt_required()
def create_event():
    event_name = request.json.get('event_name')
    
    if not event_name:
        return jsonify({"error": "Event name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO events (event_name) VALUES (?)", (event_name,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Event created successfully!"})

@event_routes.route('/api/events', methods=['GET'])
@jwt_required()
def get_events():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM events")
            events = c.fetchall()
            events_list = [dict(event) for event in events]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"events": events_list})