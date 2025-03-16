from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import Schema, fields, ValidationError

# إنشاء Blueprint للطرق المتعلقة بالتحقق
validation_routes = Blueprint('validation_routes', __name__)

# تعريف مخطط المستخدم باستخدام Marshmallow
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

# تعريف مسار للتحقق من بيانات المستخدم
@validation_routes.route('/api/validate/user', methods=['POST'])
@jwt_required()
def validate_user():
    try:
        # الحصول على البيانات من الطلب
        data = request.json
        # تحميل البيانات والتحقق منها باستخدام UserSchema
        UserSchema().load(data)
        return jsonify({"message": "Data is valid!"})
    except ValidationError as err:
        # إرجاع رسالة خطأ في حالة وجود خطأ في التحقق
        return jsonify({"error": err.messages}), 400