from flask import jsonify
from werkzeug.exceptions import HTTPException

# دالة لمعالجة أخطاء HTTP
def handle_http_error(error):
    """
    Handle HTTP exceptions and return a JSON response with the error description and status code.
    
    :param error: HTTPException instance
    :return: JSON response with error description and status code
    """
    return jsonify({
        "error": error.description,
        "status_code": error.code
    }), error.code

# دالة لمعالجة الأخطاء العامة
def handle_generic_error(error):
    """
    Handle generic exceptions and return a JSON response with a generic error message and status code 500.
    
    :param error: Exception instance
    :return: JSON response with generic error message and status code 500
    """
    return jsonify({
        "error": "An unexpected error occurred.",
        "status_code": 500
    }), 500