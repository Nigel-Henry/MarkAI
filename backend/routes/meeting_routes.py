from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

meeting_routes = Blueprint('meeting_routes', __name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@meeting_routes.route('/api/meetings', methods=['POST'])
@jwt_required()
def create_meeting():
    meeting_title = request.json.get('meeting_title')
    meeting_date = request.json.get('meeting_date')

    if not meeting_title or not meeting_date:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO meetings (meeting_title, meeting_date) VALUES (?, ?)", 
                      (meeting_title, meeting_date))
            conn.commit()
        return jsonify({"message": "Meeting created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@meeting_routes.route('/api/meetings', methods=['GET'])
@jwt_required()
def get_meetings():
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM meetings")
            meetings = c.fetchall()
        return jsonify({"meetings": meetings}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500