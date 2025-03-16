from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import pandas as pd
from werkzeug.utils import secure_filename

import_routes = Blueprint('import_routes', __name__)

@import_routes.route('/api/import/users', methods=['POST'])
@jwt_required()
def import_users():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV file: {str(e)}"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            for index, row in df.iterrows():
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (row['username'], row['password']))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Users imported successfully!"})

@import_routes.route('/api/import/knowledge', methods=['POST'])
@jwt_required()
def import_knowledge():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV file: {str(e)}"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            for index, row in df.iterrows():
                c.execute("INSERT INTO knowledge (topic, content) VALUES (?, ?)", (row['topic'], row['content']))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Knowledge imported successfully!"})