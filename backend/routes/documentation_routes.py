from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

documentation_routes = Blueprint('documentation_routes', __name__)

@documentation_routes.route('/api/documentation', methods=['POST'])
@jwt_required()
def create_documentation():
    documentation_name = request.json.get('documentation_name')
    
    if not documentation_name:
        return jsonify({"error": "documentation_name is required"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO documentation (documentation_name) VALUES (?)", (documentation_name,))
            conn.commit()
        return jsonify({"message": "Documentation created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@documentation_routes.route('/api/documentation', methods=['GET'])
@jwt_required()
def get_documentation():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM documentation")
            documentation = c.fetchall()
        return jsonify({"documentation": documentation}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500