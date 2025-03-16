# backend/src/routes/api_keys.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import secrets
import string
import sqlite3
from contextlib import closing

api_keys_bp = Blueprint('api_keys', __name__)

def generate_api_key():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(32))

def get_db_connection():
    return sqlite3.connect('markai.db')

@api_keys_bp.route('/api/generate-key', methods=['POST'])
@jwt_required()
def generate_key():
    user_id = get_jwt_identity()
    key_type = request.json.get('key_type', 'free')
    
    try:
        with get_db_connection() as conn:
            with closing(conn.cursor()) as c:
                if key_type == 'free':
                    c.execute("SELECT COUNT(*) FROM api_keys WHERE user_id = ? AND key_type = 'free'", (user_id,))
                    if c.fetchone()[0] >= 3:
                        return jsonify({"error": "Free tier limit reached"}), 400
                
                api_key = generate_api_key()
                
                c.execute("""
                    INSERT INTO api_keys (user_id, api_key, key_type, active, request_count) 
                    VALUES (?, ?, ?, 1, 0)
                """, (user_id, api_key, key_type))
                
                conn.commit()
                
        return jsonify({"api_key": api_key})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@api_keys_bp.route('/api/keys', methods=['GET'])
@jwt_required()
def get_keys():
    user_id = get_jwt_identity()
    
    try:
        with get_db_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute("""
                    SELECT api_key, key_type, created_at, request_count 
                    FROM api_keys 
                    WHERE user_id = ?
                """, (user_id,))
                
                keys = [dict(zip(['key', 'type', 'created', 'requests'], row)) for row in c.fetchall()]
                
        return jsonify({"keys": keys})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500