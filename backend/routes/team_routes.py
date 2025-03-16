from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

team_routes = Blueprint('team_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@team_routes.route('/api/teams', methods=['POST'])
@jwt_required()
def create_team():
    try:
        team_name = request.json.get('team_name')
        team_description = request.json.get('team_description')

        if not team_name or not team_description:
            return jsonify({"error": "Both team_name and team_description are required"}), 400

        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO teams (team_name, team_description) VALUES (?, ?)", 
                      (team_name, team_description))
            conn.commit()

        return jsonify({"message": "Team created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@team_routes.route('/api/teams', methods=['GET'])
@jwt_required()
def get_teams():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM teams")
            teams = c.fetchall()

        return jsonify({"teams": [dict(row) for row in teams]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500