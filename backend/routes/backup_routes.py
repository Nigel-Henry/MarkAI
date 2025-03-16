from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

backup_routes = Blueprint('backup_routes', __name__)

DATABASE = 'knowledge.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@backup_routes.route('/api/backup', methods=['POST'])
@jwt_required()
def create_backup():
    backup_name = request.json.get('backup_name')
    if not backup_name:
        return jsonify({"error": "Backup name is required"}), 400
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO backups (backup_name) VALUES (?)", (backup_name,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Backup created successfully!"}), 201

@backup_routes.route('/api/backup', methods=['GET'])
@jwt_required()
def get_backups():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM backups")
    backups = c.fetchall()
    conn.close()

    backups_list = [dict(backup) for backup in backups]
    return jsonify({"backups": backups_list}), 200