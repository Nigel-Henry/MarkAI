from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

lead_routes = Blueprint('lead_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@lead_routes.route('/api/leads', methods=['POST'])
@jwt_required()
def create_lead():
    lead_name = request.json.get('lead_name')
    if not lead_name:
        return jsonify({"error": "Lead name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO leads (lead_name) VALUES (?)", (lead_name,))
            conn.commit()
        return jsonify({"message": "Lead created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@lead_routes.route('/api/leads', methods=['GET'])
@jwt_required()
def get_leads():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM leads")
            leads = c.fetchall()
        return jsonify({"leads": [dict(row) for row in leads]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500