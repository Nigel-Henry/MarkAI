from transformers import pipeline

# إنشاء مولد النصوص مرة واحدة فقط
text_generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt, max_length=50):
    """
    توليد نص بناءً على المدخلات المقدمة.

    Args:
        prompt (str): النص المدخل.
        max_length (int): الطول الأقصى للنص المولد.

    Returns:
        str: النص المولد.
    """
    response = text_generator(prompt, max_length=max_length)
    return response[0]['generated_text']
