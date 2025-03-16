from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
import uuid

# Constants
VIDEO_FOLDER = 'videos'

# Create video folder if it doesn't exist
os.makedirs(VIDEO_FOLDER, exist_ok=True)

# Blueprint setup
video_routes = Blueprint('video_routes', __name__)

@video_routes.route('/api/videos', methods=['POST'])
@jwt_required()
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video part"}), 400
    
    video = request.files['video']
    if video.filename == '':
        return jsonify({"error": "No selected video"}), 400
    
    filename = f"{uuid.uuid4()}{os.path.splitext(video.filename)[1]}"
    video_path = os.path.join(VIDEO_FOLDER, filename)
    
    try:
        video.save(video_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Video uploaded successfully!", "filename": filename})

@video_routes.route('/api/videos', methods=['GET'])
@jwt_required()
def list_videos():
    try:
        videos = os.listdir(VIDEO_FOLDER)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"videos": videos})