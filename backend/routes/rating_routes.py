from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

rating_routes = Blueprint('rating_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@rating_routes.route('/api/ratings', methods=['POST'])
@jwt_required()
def create_rating():
    try:
        rating_value = request.json.get('rating_value')
        content_id = request.json.get('content_id')

        if rating_value is None or content_id is None:
            return jsonify({"error": "Missing rating_value or content_id"}), 400

        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO ratings (rating_value, content_id) VALUES (?, ?)", 
                      (rating_value, content_id))
            conn.commit()

        return jsonify({"message": "Rating created successfully!"}), 201

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@rating_routes.route('/api/ratings', methods=['GET'])
@jwt_required()
def get_ratings():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM ratings")
            ratings = c.fetchall()

        return jsonify({"ratings": [dict(row) for row in ratings]}), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500