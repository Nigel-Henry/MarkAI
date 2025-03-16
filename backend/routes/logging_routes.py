from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import logging
import datetime
import os

logging_routes = Blueprint('logging_routes', __name__)

# Define the absolute path for the log file
log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')

# Configure logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@logging_routes.route('/api/logs', methods=['GET'])
@jwt_required()
def get_logs():
    try:
        with open(log_file_path, 'r') as log_file:
            logs = log_file.readlines()
        return jsonify(logs)
    except Exception as e:
        logging.error(f"Error reading log file: {e}")
        return jsonify({"error": "Could not read log file"}), 500

@logging_routes.route('/api/logs/clear', methods=['POST'])
@jwt_required()
def clear_logs():
    try:
        with open(log_file_path, 'w') as log_file:
            log_file.write('')
        return jsonify({"message": "Logs cleared!"})
    except Exception as e:
        logging.error(f"Error clearing log file: {e}")
        return jsonify({"error": "Could not clear log file"}), 500

@logging_routes.route('/api/logs/add', methods=['POST'])
@jwt_required()
def add_log():
    message = request.json.get('message')
    if not message:
        return jsonify({"error": "Message is required"}), 400
    try:
        logging.info(message)
        return jsonify({"message": "Log added successfully!"})
    except Exception as e:
        logging.error(f"Error adding log: {e}")
        return jsonify({"error": "Could not add log"}), 500