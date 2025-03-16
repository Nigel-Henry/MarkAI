from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from gtts import gTTS
from moviepy.editor import TextClip
from transformers import pipeline
import os

# Create a Blueprint for AI-related routes
ai_routes = Blueprint('ai_routes', __name__)

# Setup Rate Limiting
limiter = Limiter(key_func=lambda: request.remote_addr)

# Load text generation model
text_generator = pipeline("text-generation")

# List of supported languages
SUPPORTED_LANGUAGES = {
    "ar": "Arabic",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh": "Chinese",
    "ja": "Japanese",
    "ru": "Russian",
    # Add more languages here if needed
}

# Route for text generation
@ai_routes.route('/api/generate/text', methods=['POST'])
@jwt_required()
@limiter.limit("10/minute")
def generate_text():
    data = request.json
    text = data.get('text')
    language = data.get('language', 'en')  # Default language is English
    
    if not text:
        return jsonify({"error": "Text is required!"}), 400
    
    # Generate text using the model
    generated_text = text_generator(text, max_length=50, num_return_sequences=1)[0]['generated_text']
    return jsonify({"result": generated_text, "language": language})

# Route for speech generation
@ai_routes.route('/api/generate/speech', methods=['POST'])
@jwt_required()
def generate_speech():
    data = request.json
    text = data.get('text')
    language = data.get('language', 'en')  # Default language is English
    
    if not text:
        return jsonify({"error": "Text is required!"}), 400
    
    if language not in SUPPORTED_LANGUAGES:
        return jsonify({"error": "Unsupported language!"}), 400
    
    # Generate speech using gTTS
    tts = gTTS(text=text, lang=language)
    output_file = f"output_{language}.mp3"
    tts.save(output_file)
    
    # Send the file as a response
    response = send_file(output_file, as_attachment=True)
    
    # Remove the file after sending
    os.remove(output_file)
    return response

# Route for video generation
@ai_routes.route('/api/generate/video', methods=['POST'])
@jwt_required()
def generate_video():
    data = request.json
    text = data.get('text')
    language = data.get('language', 'en')  # Default language is English
    
    if not text:
        return jsonify({"error": "Text is required!"}), 400
    
    # Create a video clip using moviepy
    clip = TextClip(text, fontsize=50, color='white', size=(1280, 720))
    clip = clip.set_duration(10)  # Video duration is 10 seconds
    output_file = f"output_{language}.mp4"
    clip.write_videofile(output_file, fps=24)
    
    # Send the file as a response
    response = send_file(output_file, as_attachment=True)
    
    # Remove the file after sending
    os.remove(output_file)
    return response