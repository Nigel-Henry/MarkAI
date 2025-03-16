from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
import uuid

# Constants
UPLOAD_FOLDER = 'uploads'

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Blueprint setup
file_routes = Blueprint('file_routes', __name__)

@file_routes.route('/api/files', methods=['POST'])
@jwt_required()
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Generate a unique filename
    filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
    
    # Save the file
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    
    return jsonify({"message": "File uploaded successfully!", "filename": filename})

@file_routes.route('/api/files', methods=['GET'])
@jwt_required()
def list_files():
    # List files in the upload folder
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"files": files})