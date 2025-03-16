from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import sqlite3
import os

update_routes = Blueprint('update_routes', __name__)

# استخدم متغير بيئة لتحديد مسار قاعدة البيانات
DATABASE_PATH = os.getenv('DATABASE_PATH', 'knowledge.db')

@update_routes.route('/api/updates', methods=['GET'])
@jwt_required()
def get_updates():
    # استخدم إدارة السياق للاتصال بقاعدة البيانات
    with sqlite3.connect(DATABASE_PATH) as conn:
        c = conn.cursor()
        
        # جلب آخر التحديثات
        c.execute("SELECT * FROM updates ORDER BY release_date DESC")
        updates = c.fetchall()
    
    # إرجاع البيانات كـ JSON
    return jsonify({
        "version": "1.0.0",
        "updates": updates,
        "release_notes": "Initial release of MarkAI."
    })
