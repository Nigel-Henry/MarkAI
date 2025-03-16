from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required
import sqlite3
import pandas as pd
import os

export_routes = Blueprint('export_routes', __name__)

DATABASE_PATH = 'knowledge.db'
EXPORT_DIR = 'exports'

def export_table_to_csv(table_name, export_filename):
    try:
        os.makedirs(EXPORT_DIR, exist_ok=True)
        export_path = os.path.join(EXPORT_DIR, export_filename)
        with sqlite3.connect(DATABASE_PATH) as conn:
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            df.to_csv(export_path, index=False)
        return send_file(export_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@export_routes.route('/api/export/users', methods=['GET'])
@jwt_required()
def export_users():
    return export_table_to_csv('users', 'users_export.csv')

@export_routes.route('/api/export/knowledge', methods=['GET'])
@jwt_required()
def export_knowledge():
    return export_table_to_csv('knowledge', 'knowledge_export.csv')