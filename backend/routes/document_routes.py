from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import os
import uuid

# Constants
DOCUMENT_FOLDER = 'documents'

# Ensure the document folder exists
os.makedirs(DOCUMENT_FOLDER, exist_ok=True)

# Blueprint setup
document_routes = Blueprint('document_routes', __name__)

@document_routes.route('/api/documents', methods=['POST'])
@jwt_required()
def upload_document():
    if 'document' not in request.files:
        return jsonify({"error": "No document part"}), 400
    
    document = request.files['document']
    if document.filename == '':
        return jsonify({"error": "No selected document"}), 400
    
    filename = str(uuid.uuid4()) + os.path.splitext(document.filename)[1]
    document.save(os.path.join(DOCUMENT_FOLDER, filename))
    
    return jsonify({"message": "Document uploaded successfully!", "filename": filename})

@document_routes.route('/api/documents', methods=['GET'])
@jwt_required()
def list_documents():
    documents = os.listdir(DOCUMENT_FOLDER)
    return jsonify({"documents": documents})