from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

certificate_routes = Blueprint('certificate_routes', __name__)

DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@certificate_routes.route('/api/certificates', methods=['POST'])
@jwt_required()
def create_certificate():
    certificate_name = request.json.get('certificate_name')
    if not certificate_name:
        return jsonify({"error": "Certificate name is required"}), 400

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO certificates (certificate_name) VALUES (?)", (certificate_name,))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Certificate created successfully!"})

@certificate_routes.route('/api/certificates', methods=['GET'])
@jwt_required()
def get_certificates():
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM certificates")
            certificates = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"certificates": certificates})