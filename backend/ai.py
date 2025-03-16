from flask import Blueprint, request, jsonify
from transformers import pipeline
import os

# إنشاء Blueprint
bp = Blueprint('ai', __name__)

# تحميل النموذج من Hugging Face
model_name = os.getenv('MODEL_NAME', 'gpt2')
chatbot = pipeline('text-generation', model=model_name)

@bp.route('/api/ai/chat', methods=['POST'])
def chat():
    # الحصول على المدخلات من الطلب
    prompt = request.json.get('prompt')
    
    # التحقق من أن المدخلات ليست فارغة
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    # توليد النص باستخدام النموذج
    response = chatbot(prompt, max_length=100)[0]['generated_text']
    
    # إرجاع الاستجابة كـ JSON
    return jsonify({"response": response})