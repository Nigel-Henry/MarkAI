from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.api_key_model import APIKey
from ..utils.api_key_generator import generate_api_key
import sqlite3

integration_routes = Blueprint('integration_routes', __name__)

@integration_routes.route('/api/generate-key', methods=['POST'])
@jwt_required()
def generate_key():
    user_id = get_jwt_identity()
    key_type = request.json.get('key_type', 'free')  # 'free' or 'paid'
    api_key = generate_api_key()

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO api_keys (user_id, api_key, key_type) VALUES (?, ?, ?)", 
                      (user_id, api_key, key_type))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"api_key": api_key, "key_type": key_type})

@integration_routes.route('/api/validate-key', methods=['POST'])
def validate_key():
    api_key = request.json.get('api_key')

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM api_keys WHERE api_key = ?", (api_key,))
            key_data = c.fetchone()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    if key_data:
        return jsonify({"valid": True, "key_type": key_data[3]})
    return jsonify({"valid": False}), 401