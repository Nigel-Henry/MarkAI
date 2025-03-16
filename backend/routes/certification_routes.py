from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

certification_routes = Blueprint('certification_routes', __name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@certification_routes.route('/api/certifications', methods=['POST'])
@jwt_required()
def create_certification():
    certification_name = request.json.get('certification_name')
    if not certification_name:
        return jsonify({"error": "Certification name is required"}), 400

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO certifications (certification_name) VALUES (?)", (certification_name,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Certification created successfully!"})

@certification_routes.route('/api/certifications', methods=['GET'])
@jwt_required()
def get_certifications():
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM certifications")
            certifications = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"certifications": certifications})