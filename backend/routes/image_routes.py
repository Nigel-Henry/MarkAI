from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
import uuid
from PIL import Image
from werkzeug.utils import secure_filename

# Define the blueprint
image_routes = Blueprint('image_routes', __name__)

# Define the folder to store images
IMAGE_FOLDER = 'images'
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@image_routes.route('/api/images', methods=['POST'])
@jwt_required()
def upload_image():
    # Check if the image part is in the request
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400
    
    image = request.files['image']
    
    # Check if the image has a filename
    if image.filename == '':
        return jsonify({"error": "No selected image"}), 400
    
    # Generate a secure filename
    filename = secure_filename(str(uuid.uuid4()) + os.path.splitext(image.filename)[1])
    
    try:
        # Save the image to the folder
        image.save(os.path.join(IMAGE_FOLDER, filename))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Image uploaded successfully!", "filename": filename})

@image_routes.route('/api/images', methods=['GET'])
@jwt_required()
def list_images():
    try:
        # List all images in the folder
        images = os.listdir(IMAGE_FOLDER)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"images": images})