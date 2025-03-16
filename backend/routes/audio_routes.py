from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
import uuid

audio_routes = Blueprint('audio_routes', __name__)
AUDIO_FOLDER = 'audios'
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@audio_routes.route('/api/audios', methods=['POST'])
@jwt_required()
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio part"}), 400
    audio = request.files['audio']
    if audio.filename == '':
        return jsonify({"error": "No selected audio"}), 400
    filename = str(uuid.uuid4()) + os.path.splitext(audio.filename)[1]
    audio.save(os.path.join(AUDIO_FOLDER, filename))
    return jsonify({"message": "Audio uploaded successfully!", "filename": filename}), 201

@audio_routes.route('/api/audios', methods=['GET'])
@jwt_required()
def list_audios():
    audios = os.listdir(AUDIO_FOLDER)
    return jsonify({"audios": audios}), 200