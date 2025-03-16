from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import sqlite3

# إنشاء Blueprint لتنظيم routes
permission_routes = Blueprint('permission_routes', __name__)

# وظيفة مساعدة للتعامل مع اتصالات قاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row  # للحصول على نتائج كـ dictionaries بدلاً من tuples
    return conn

# إنشاء إذن جديد
@permission_routes.route('/api/permissions', methods=['POST'])
@jwt_required()
def create_permission():
    permission_name = request.json.get('permission_name')

    # التحقق من صحة البيانات
    if not permission_name:
        return jsonify({"error": "Permission name is required"}), 400

    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO permissions (permission_name) VALUES (?)", (permission_name,))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        conn.close()

    return jsonify({"message": "Permission created successfully!", "permission_name": permission_name}), 201

# الحصول على جميع الأذونات
@permission_routes.route('/api/permissions', methods=['GET'])
@jwt_required()
def get_permissions():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM permissions")
        permissions = c.fetchall()

        # تحويل النتائج إلى قائمة من dictionaries
        permissions_list = [dict(row) for row in permissions]
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        conn.close()

    return jsonify({"permissions": permissions_list})
