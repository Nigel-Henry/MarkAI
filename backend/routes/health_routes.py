from flask import Blueprint, jsonify
import psutil

# Create a Blueprint for health routes
health_routes = Blueprint('health_routes', __name__)

@health_routes.route('/api/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health of the system.
    Returns the CPU, memory, and disk usage as a JSON response.
    """
    # Get system usage statistics
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    # Return the statistics as a JSON response
    return jsonify({
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage
    })