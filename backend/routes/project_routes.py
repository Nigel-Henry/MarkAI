from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

project_routes = Blueprint('project_routes', __name__)

def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row
    return conn

@project_routes.route('/api/projects', methods=['POST'])
@jwt_required()
def create_project():
    data = request.get_json()
    project_name = data.get('project_name')
    project_description = data.get('project_description')

    if not project_name or not project_description:
        return jsonify({"error": "Project name and description are required"}), 400

    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO projects (project_name, project_description) VALUES (?, ?)", 
                      (project_name, project_description))
            conn.commit()
        return jsonify({"message": "Project created successfully!"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@project_routes.route('/api/projects', methods=['GET'])
@jwt_required()
def get_projects():
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM projects")
            projects = c.fetchall()
            projects_list = [dict(row) for row in projects]
        return jsonify({"projects": projects_list}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500