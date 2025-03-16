from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

risk_routes = Blueprint('risk_routes', __name__)

@risk_routes.route('/api/risks', methods=['POST'])
@jwt_required()
def create_risk():
    risk_name = request.json.get('risk_name')
    risk_description = request.json.get('risk_description')

    if not risk_name or not risk_description:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO risks (risk_name, risk_description) VALUES (?, ?)", 
                      (risk_name, risk_description))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Risk created successfully!"}), 201

@risk_routes.route('/api/risks', methods=['GET'])
@jwt_required()
def get_risks():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM risks")
            risks = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"risks": risks}), 200