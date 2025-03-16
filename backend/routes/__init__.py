# هذا الملف يحتوي على جميع المسارات المتوفرة في التطبيق

# هذا الملف يحتوي على جميع المسارات المتوفرة في التطبيق

from .auth_routes import auth_routes
from .knowledge_routes import knowledge_routes
from .file_routes import file_routes
from .ai_routes import ai_routes
from .cloud_routes import cloud_routes
from .payment_routes import payment_routes
from .analytics_routes import analytics_routes
from .social_routes import social_routes
from .ocr_routes import ocr_routes
from .encryption_routes import encryption_routes
from .spotify_routes import spotify_routes
from .chatbot_routes import chatbot_routes
from .speech_routes import speech_routes
from .mongodb_routes import mongodb_routes
from .websocket_routes import websocket_routes
from .notification_routes import notification_routes
from .logging_routes import logging_routes
from .backup_routes import backup_routes
from .health_routes import health_routes
from .security_routes import security_routes
from .admin_routes import admin_routes
from .feedback_routes import feedback_routes
from .report_routes import report_routes
from .export_routes import export_routes
from .import_routes import import_routes
from .validation_routes import validation_routes
from .authentication_routes import authentication_routes
from .authorization_routes import authorization_routes
from .performance_routes import performance_routes
from .caching_routes import caching_routes
from .queue_routes import queue_routes
from .background_tasks import background_tasks
from .scheduler_routes import scheduler_routes
from .versioning_routes import versioning_routes
from .documentation_routes import documentation_routes
from .monitoring_routes import monitoring_routes

# تسجيل جميع المسارات
all_routes = [
    auth_routes,
    knowledge_routes,
    file_routes,
    ai_routes,
    cloud_routes,
    payment_routes,
    analytics_routes,
    social_routes,
    ocr_routes,
    encryption_routes,
    spotify_routes,
    chatbot_routes,
    speech_routes,
    mongodb_routes,
    websocket_routes,
    notification_routes,
    logging_routes,
    backup_routes,
    health_routes,
    security_routes,
    admin_routes,
    feedback_routes,
    report_routes,
    export_routes,
    import_routes,
    validation_routes,
    authentication_routes,
    authorization_routes,
    performance_routes,
    caching_routes,
    queue_routes,
    background_tasks,
    scheduler_routes,
    versioning_routes,
    documentation_routes,
    monitoring_routes
]