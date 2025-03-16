from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

comment_routes = Blueprint('comment_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@comment_routes.route('/api/comments', methods=['POST'])
@jwt_required()
def create_comment():
    comment_text = request.json.get('comment_text')
    content_id = request.json.get('content_id')

    if not comment_text or not content_id:
        return jsonify({"error": "Missing comment_text or content_id"}), 400

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO comments (comment_text, content_id) VALUES (?, ?)", 
              (comment_text, content_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Comment created successfully!"}), 201

@comment_routes.route('/api/comments', methods=['GET'])
@jwt_required()
def get_comments():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM comments")
    comments = c.fetchall()
    conn.close()

    comments_list = [dict(comment) for comment in comments]

    return jsonify({"comments": comments_list}), 200