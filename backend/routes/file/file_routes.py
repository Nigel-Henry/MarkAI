from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
import os

# إنشاء Blueprint للمسارات الخاصة بإدارة الملفات
file_routes = Blueprint('file_routes', __name__)

# مجلد التحميل
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# مسار لتحميل الملفات
@file_routes.route('/api/upload', methods=['POST'])
@jwt_required()
def upload_file():
    try:
        # التحقق من وجود الملف في الطلب
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        
        # التحقق من وجود اسم الملف
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        # تأمين اسم الملف وحفظه
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        return jsonify({"message": "File uploaded successfully!", "filename": filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# مسار لسرد الملفات
@file_routes.route('/api/files', methods=['GET'])
@jwt_required()
def list_files():
    try:
        # جرد الملفات في مجلد التحميل
        files = os.listdir(UPLOAD_FOLDER)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# مسار لتنزيل الملفات
@file_routes.route('/api/files/<filename>', methods=['GET'])
@jwt_required()
def download_file(filename):
    try:
        # التحقق من وجود الملف
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found!"}), 404
        
        # إرسال الملف كاستجابة
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500