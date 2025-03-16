from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

search_routes = Blueprint('search_routes', __name__)

# Assuming the database path is stored in an environment variable
DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@search_routes.route('/api/search', methods=['GET'])
@jwt_required()
def search():
    query = request.args.get('q')
    
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM knowledge WHERE topic LIKE ?", ('%' + query + '%',))
            results = c.fetchall()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"results": results})