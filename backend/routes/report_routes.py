from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

report_routes = Blueprint('report_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@report_routes.route('/api/reports', methods=['POST'])
@jwt_required()
def create_report():
    report_name = request.json.get('report_name')
    if not report_name:
        return jsonify({"error": "Report name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO reports (report_name) VALUES (?)", (report_name,))
            conn.commit()
        return jsonify({"message": "Report created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@report_routes.route('/api/reports', methods=['GET'])
@jwt_required()
def get_reports():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM reports")
            reports = c.fetchall()
        return jsonify({"reports": [dict(row) for row in reports]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500