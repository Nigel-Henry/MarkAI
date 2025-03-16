from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import pyotp
import sqlite3

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/api/enable-2fa', methods=['POST'])
@jwt_required()
def enable_2fa():
    user_id = get_jwt_identity()
    secret = pyotp.random_base32()
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE users SET twofa_secret = ? WHERE id = ?", (secret, user_id))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"secret": secret})

@auth_routes.route('/api/verify-2fa', methods=['POST'])
@jwt_required()
def verify_2fa():
    user_id = get_jwt_identity()
    token = request.json.get('token')
    
    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT twofa_secret FROM users WHERE id = ?", (user_id,))
            user = c.fetchone()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    if user and pyotp.TOTP(user[0]).verify(token):
        return jsonify({"message": "2FA verified successfully!"})
    return jsonify({"error": "Invalid 2FA token!"}), 400