from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

knowledge_routes = Blueprint('knowledge_routes', __name__)

@knowledge_routes.route('/api/knowledge', methods=['POST'])
@jwt_required()
def create_knowledge():
    knowledge_title = request.json.get('knowledge_title')
    knowledge_content = request.json.get('knowledge_content')

    if not knowledge_title or not knowledge_content:
        return jsonify({"error": "Both title and content are required"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO knowledge (knowledge_title, knowledge_content) VALUES (?, ?)", 
                      (knowledge_title, knowledge_content))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Knowledge created successfully!"}), 201

@knowledge_routes.route('/api/knowledge', methods=['GET'])
@jwt_required()
def get_knowledge():
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM knowledge")
            knowledge = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"knowledge": knowledge}), 200