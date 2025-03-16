from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlite3
from contextlib import closing

# إنشاء Blueprint للمسارات الإدارية
admin_routes = Blueprint('admin_routes', __name__)

# دالة مساعدة للتحقق من صلاحية المستخدم
def is_admin(username):
    with closing(sqlite3.connect('knowledge.db')) as conn:
        with closing(conn.cursor()) as c:
            c.execute("SELECT role FROM users WHERE username = ?", (username,))
            user = c.fetchone()
    return user and user[0] == 'admin'

# مسار لجلب جميع المستخدمين
@admin_routes.route('/api/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    username = get_jwt_identity()
    
    # التحقق من صلاحية المستخدم
    if not is_admin(username):
        return jsonify({"error": "Unauthorized!"}), 403
    
    # جلب جميع المستخدمين
    with closing(sqlite3.connect('knowledge.db')) as conn:
        with closing(conn.cursor()) as c:
            c.execute("SELECT id, username, role FROM users")
            users = c.fetchall()
    
    # تحويل النتائج إلى قائمة من القواميس
    users_list = [{"id": user[0], "username": user[1], "role": user[2]} for user in users]
    return jsonify(users_list)

# مسار لحذف مستخدم
@admin_routes.route('/api/admin/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    username = get_jwt_identity()
    
    # التحقق من صلاحية المستخدم
    if not is_admin(username):
        return jsonify({"error": "Unauthorized!"}), 403
    
    # حذف المستخدم
    conn = sqlite3.connect('knowledge.db')
    with closing(sqlite3.connect('knowledge.db')) as conn:
        with closing(conn.cursor()) as c:
            c.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
    return jsonify({"message": "User deleted successfully!"})

# مسار لتحديث دور المستخدم
@admin_routes.route('/api/admin/users/<int:user_id>/role', methods=['PUT'])
@jwt_required()
def update_user_role(user_id):
    username = get_jwt_identity()
    
    # التحقق من صلاحية المستخدم
    if not is_admin(username):
        return jsonify({"error": "Unauthorized!"}), 403
    
    # جلب البيانات من الطلب
    data = request.get_json()
    new_role = data.get('role')
    
    if not new_role:
        return jsonify({"error": "Role is required!"}), 400
    
    # تحديث دور المستخدم
    conn = sqlite3.connect('knowledge.db')
    c = conn.cursor()
    with closing(sqlite3.connect('knowledge.db')) as conn:
        with closing(conn.cursor()) as c:
            c.execute("UPDATE users SET role = ? WHERE id = ?", (new_role, user_id))
            conn.commit()
