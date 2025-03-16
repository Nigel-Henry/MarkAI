from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

media_routes = Blueprint('media_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@media_routes.route('/api/media', methods=['POST'])
@jwt_required()
def upload_media():
    media_name = request.json.get('media_name')
    media_url = request.json.get('media_url')
    
    if not media_name or not media_url:
        return jsonify({"error": "media_name and media_url are required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO media (media_name, media_url) VALUES (?, ?)", 
                      (media_name, media_url))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Media uploaded successfully!"})

@media_routes.route('/api/media', methods=['GET'])
@jwt_required()
def get_media():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM media")
            media = c.fetchall()
            media_list = [dict(row) for row in media]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"media": media_list})