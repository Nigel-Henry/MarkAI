from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from werkzeug.utils import secure_filename
import os

cloud_routes = Blueprint('cloud_routes', __name__)

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file('service-account.json')
    return build('drive', 'v3', credentials=creds)

@cloud_routes.route('/api/drive/upload', methods=['POST'])
@jwt_required()
def drive_upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(file.filename)
    file.save(filename)
    service = get_drive_service()
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename)
    uploaded = service.files().create(body=file_metadata, media_body=media).execute()
    return jsonify({"file_id": uploaded.get('id')})
