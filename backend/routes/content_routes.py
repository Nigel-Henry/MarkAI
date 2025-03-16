from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

content_routes = Blueprint('content_routes', __name__)

@content_routes.route('/api/content', methods=['POST'])
@jwt_required()
def create_content():
    content_title = request.json.get('content_title')
    content_body = request.json.get('content_body')
    
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("INSERT INTO content (content_title, content_body) VALUES (?, ?)", 
              (content_title, content_body))
    conn.commit()
    conn.close()

    return jsonify({"message": "Content created successfully!"})

@content_routes.route('/api/content', methods=['GET'])
@jwt_required()
def get_content():
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("SELECT * FROM content")
    content = c.fetchall()
    conn.close()

    return jsonify({"content": content})