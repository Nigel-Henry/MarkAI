from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

training_routes = Blueprint('training_routes', __name__)

DATABASE = 'knowledge.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@training_routes.route('/api/trainings', methods=['POST'])
@jwt_required()
def create_training():
    training_name = request.json.get('training_name')
    if not training_name:
        return jsonify({"error": "Training name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO trainings (training_name) VALUES (?)", (training_name,))
            conn.commit()
        return jsonify({"message": "Training created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@training_routes.route('/api/trainings', methods=['GET'])
@jwt_required()
def get_trainings():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM trainings")
            trainings = c.fetchall()
        return jsonify({"trainings": [dict(row) for row in trainings]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500