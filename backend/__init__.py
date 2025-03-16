from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from flask_dance.contrib.google import google_blueprint
from werkzeug.exceptions import HTTPException

from .config import Config
from .routes import (
    auth_routes, knowledge_routes, file_routes, ai_routes, cloud_routes,
    payment_routes, analytics_routes, social_routes, ocr_routes,
    encryption_routes, spotify_routes, chatbot_routes, speech_routes,
    mongodb_routes, websocket_routes, notification_routes, logging_routes,
    backup_routes, health_routes, security_routes, admin_routes,
    feedback_routes, report_routes, export_routes, import_routes,
    validation_routes, authentication_routes, authorization_routes,
    performance_routes, caching_routes, queue_routes, background_tasks,
    scheduler_routes, versioning_routes, documentation_routes, auth, 
    users, roles, tasks, notifications,
    reports, permissions, events, logs, settings,
    content, comments, ratings, clients, sales,
    inventory, projects, team, files, media,
    analytics, security, backups, documentation,
    certifications, training, complaints, marketing,
    leads, campaigns, ai
)
from .error_handlers import handle_http_error, handle_generic_error

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_routes)
    app.register_blueprint(knowledge_routes)
    app.register_blueprint(file_routes)
    app.register_blueprint(ai_routes)
    app.register_blueprint(cloud_routes)
    app.register_blueprint(payment_routes)
    app.register_blueprint(analytics_routes)
    app.register_blueprint(social_routes)
    app.register_blueprint(ocr_routes)
    app.register_blueprint(encryption_routes)
    app.register_blueprint(spotify_routes)
    app.register_blueprint(chatbot_routes)
    app.register_blueprint(speech_routes)
    app.register_blueprint(mongodb_routes)
    app.register_blueprint(websocket_routes)
    app.register_blueprint(notification_routes)
    app.register_blueprint(logging_routes)
    app.register_blueprint(backup_routes)
    app.register_blueprint(health_routes)
    app.register_blueprint(security_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(feedback_routes)
    app.register_blueprint(report_routes)
    app.register_blueprint(export_routes)
    app.register_blueprint(import_routes)
    app.register_blueprint(validation_routes)
    app.register_blueprint(authentication_routes)
    app.register_blueprint(authorization_routes)
    app.register_blueprint(performance_routes)
    app.register_blueprint(caching_routes)
    app.register_blueprint(queue_routes)
    app.register_blueprint(background_tasks)
    app.register_blueprint(scheduler_routes)
    app.register_blueprint(versioning_routes)
    app.register_blueprint(documentation_routes)
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(roles)
    app.register_blueprint(tasks)
    app.register_blueprint(notifications)
    app.register_blueprint(reports)
    app.register_blueprint(permissions)
    app.register_blueprint(events)
    app.register_blueprint(logs)
    app.register_blueprint(settings)
    app.register_blueprint(content)
    app.register_blueprint(comments)
    app.register_blueprint(ratings)
    app.register_blueprint(clients)
    app.register_blueprint(sales)
    app.register_blueprint(inventory)
    app.register_blueprint(projects)
    app.register_blueprint(team)
    app.register_blueprint(files)
    app.register_blueprint(media)
    app.register_blueprint(analytics)
    app.register_blueprint(security)
    app.register_blueprint(backups)
    app.register_blueprint(documentation)
    app.register_blueprint(certifications)
    app.register_blueprint(training)
    app.register_blueprint(complaints)
    app.register_blueprint(marketing)
    app.register_blueprint(leads)
    app.register_blueprint(campaigns)
    app.register_blueprint(ai)

    # Register Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Register Google OAuth
    app.register_blueprint(google_blueprint, url_prefix='/api/auth')

    # Error handlers
    app.register_error_handler(HTTPException, handle_http_error)
    app.register_error_handler(Exception, handle_generic_error)
    
    return app
