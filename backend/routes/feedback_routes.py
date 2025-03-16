from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3

feedback_routes = Blueprint('feedback_routes', __name__)

@feedback_routes.route('/api/feedback', methods=['POST'])
@jwt_required()
def submit_feedback():
    try:
        username = get_jwt_identity()
        feedback = request.json.get('feedback')
        
        if not feedback:
            return jsonify({"error": "Feedback is required"}), 400
        
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO feedback (username, feedback) VALUES (?, ?)", (username, feedback))
            conn.commit()
        
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@feedback_routes.route('/api/feedback', methods=['GET'])
@jwt_required()
def get_feedback():
    try:
        username = get_jwt_identity()
        
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM feedback WHERE username = ?", (username,))
            feedback = c.fetchall()
        
        return jsonify(feedback), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500