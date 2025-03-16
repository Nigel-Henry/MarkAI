from flask import Blueprint, jsonify, request
from ..utils.export_utils import export_data

# إنشاء Blueprint لتوجيهات التصدير
export_bp = Blueprint('export', __name__)

@export_bp.route('/export', methods=['POST'])
def export_data_route():
    """
    Route to handle data export requests.
    """
    try:
        # استدعاء دالة التصدير
        export_data()
        return jsonify({"message": "Data exported successfully"}), 200
    except Exception as e:
        # إرجاع رسالة خطأ في حالة حدوث استثناء
        return jsonify({"error": str(e)}), 500