# /home/mark/MarkAi/backend/app.py

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from datetime import timedelta
import os
import redis
from werkzeug.exceptions import HTTPException
from config.config import Config
from routes import register_blueprints
from error_handlers import handle_http_error, handle_generic_error
from flask_swagger_ui import get_swaggerui_blueprint
from flask_dance.contrib.google import google_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address)
CORS(app)

# Register blueprints
register_blueprints(app)

# Error handlers
app.register_error_handler(HTTPException, handle_http_error)
app.register_error_handler(Exception, handle_generic_error)

# Swagger UI setup
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Google OAuth setup
google_bp = google_blueprint(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    redirect_to='google_login'
)
app.register_blueprint(google_bp, url_prefix='/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
