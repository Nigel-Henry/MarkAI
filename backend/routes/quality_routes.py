from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

quality_routes = Blueprint('quality_routes', __name__)

@quality_routes.route('/api/quality', methods=['POST'])
@jwt_required()
def create_quality():
    data = request.get_json()
    quality_name = data.get('quality_name')
    quality_description = data.get('quality_description')

    if not quality_name or not quality_description:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO quality (quality_name, quality_description) VALUES (?, ?)", 
                      (quality_name, quality_description))
            conn.commit()
        return jsonify({"message": "Quality created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@quality_routes.route('/api/quality', methods=['GET'])
@jwt_required()
def get_quality():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM quality")
            quality = c.fetchall()
        return jsonify({"quality": quality}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500