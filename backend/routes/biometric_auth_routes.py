# backend/routes/biometric_auth_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import sqlite3
import hashlib

biometric_auth_routes = Blueprint('biometric_auth_routes', __name__)

def generate_biometric_key(face_data):
    """
    Generate a biometric key using SHA-256 hash of the face data.
    """
    return hashlib.sha256(face_data.encode()).hexdigest()

def verify_biometric_key(stored_key, input_face_data):
    """
    Verify the biometric key by comparing the stored key with the generated key from input face data.
    """
    input_key = generate_biometric_key(input_face_data)
    return stored_key == input_key

@biometric_auth_routes.route('/api/biometric/enroll', methods=['POST'])
@jwt_required()
def enroll_biometric():
    """
    Enroll biometric data for the authenticated user.
    """
    username = get_jwt_identity()
    face_data = request.json.get('face_data')

    if not face_data:
        return jsonify({"error": "Face data is required!"}), 400

    biometric_key = generate_biometric_key(face_data)

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE users SET biometric_key = ? WHERE username = ?", (biometric_key, username))
            conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Biometric enrollment successful!"})

@biometric_auth_routes.route('/api/biometric/authenticate', methods=['POST'])
def authenticate_biometric():
    """
    Authenticate user using biometric data.
    """
    username = request.json.get('username')
    face_data = request.json.get('face_data')

    if not username or not face_data:
        return jsonify({"error": "Username and face data are required!"}), 400

    try:
        with sqlite3.connect('knowledge.db') as conn:
            c = conn.cursor()
            c.execute("SELECT biometric_key FROM users WHERE username = ?", (username,))
            user = c.fetchone()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

    if not user or not user[0]:
        return jsonify({"error": "User not enrolled for biometric authentication!"}), 404

    if verify_biometric_key(user[0], face_data):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Biometric authentication failed!"}), 401