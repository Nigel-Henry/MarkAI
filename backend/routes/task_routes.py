from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

task_routes = Blueprint('task_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@task_routes.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    task_name = request.json.get('task_name')
    if not task_name:
        return jsonify({"error": "Task name is required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task_name) VALUES (?)", (task_name,))
            conn.commit()
        return jsonify({"message": "Task created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@task_routes.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tasks")
            tasks = c.fetchall()
        return jsonify({"tasks": [dict(task) for task in tasks]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500