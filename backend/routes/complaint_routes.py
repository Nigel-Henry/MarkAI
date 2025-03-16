from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

complaint_routes = Blueprint('complaint_routes', __name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@complaint_routes.route('/api/complaints', methods=['POST'])
@jwt_required()
def create_complaint():
    complaint_message = request.json.get('complaint_message')
    if not complaint_message:
        return jsonify({"error": "Complaint message is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO complaints (complaint_message) VALUES (?)", (complaint_message,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Complaint created successfully!"})

@complaint_routes.route('/api/complaints', methods=['GET'])
@jwt_required()
def get_complaints():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM complaints")
            complaints = c.fetchall()
            complaints = [dict(row) for row in complaints]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"complaints": complaints})