from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

# Initialize the blueprint
tips_routes = Blueprint('tips_routes', __name__)

# Define the route for getting tips
@tips_routes.route('/api/tips', methods=['GET'])
@jwt_required()
def get_tips():
    try:
        tips = [
            "💡 يمكنك استخدام /help لرؤية الأوامر المتاحة",
            "🔍 ابحث في ويكيبيديا بكتابة /wiki موضوعك",
            "🎥 استخدم /video لإنشاء فيديو من النص"
        ]
        return jsonify(tips), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500