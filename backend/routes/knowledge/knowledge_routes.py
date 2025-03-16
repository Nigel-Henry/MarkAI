from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import wikipedia
import sqlite3

knowledge_routes = Blueprint('knowledge_routes', __name__)

@knowledge_routes.route('/api/wiki', methods=['GET'])
@jwt_required()
def wiki_search():
    query = request.args.get('q')
    try:
        summary = wikipedia.summary(query)
        return jsonify({"result": summary})
    except wikipedia.exceptions.PageError:
        return jsonify({"error": "No page found"}), 404
    except wikipedia.exceptions.DisambiguationError as e:
        return jsonify({"error": "Multiple results found", "options": e.options}), 400

@knowledge_routes.route('/api/knowledge', methods=['POST'])
@jwt_required()
def add_knowledge():
    data = request.json
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("INSERT INTO knowledge (topic, content) VALUES (?, ?)", 
              (data['topic'], data['content']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Knowledge added!"}), 201

@knowledge_routes.route('/api/knowledge/search', methods=['GET'])
@jwt_required()
def search_knowledge():
    query = request.args.get('q')
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    c.execute("SELECT * FROM knowledge WHERE topic LIKE ?", ('%'+query+'%',))
    results = c.fetchall()
    conn.close()
    return jsonify(results)
