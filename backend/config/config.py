import os
from dotenv import load_dotenv
from datetime import timedelta

# تحميل المتغيرات من ملف .env
load_dotenv()

class Config:
    # إعدادات عامة
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 1)))  # افتراضي: 1 ساعة

    # قاعدة البيانات
    DB_ENGINE = os.getenv("DB_ENGINE", "sqlite")  # افتراضي: sqlite
    DB_NAME = os.getenv("DB_NAME", "markai.db")  # افتراضي: markai.db
    DB_USER = os.getenv("DB_USER", "user")  # افتراضي: user
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")  # افتراضي: password
    DB_HOST = os.getenv("DB_HOST", "localhost")  # افتراضي: localhost
    DB_PORT = os.getenv("DB_PORT", "5432")  # افتراضي: 5432

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', {
        'sqlite': f'sqlite:///{DB_NAME}',
        'postgresql': f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    }.get(DB_ENGINE, 'sqlite'))  # افتراضي: sqlite

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # تعطيل تعديلات SQLAlchemy

    # Redis للتخزين المؤقت
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    # إعدادات التحميل
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")  # افتراضي: uploads
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024))  # افتراضي: 16MB

    # مفاتيح APIs
    GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")  # مفتاح Google Search API
    GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")  # Google Custom Search Engine ID
    GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")  # GitHub Access Token
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")  # Twitter API Key
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")  # Twitter API Secret
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")  # Twitter Bearer Token
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")  # Spotify Client ID
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")  # Spotify Client Secret
    FACEBOOK_APP_ID = os.getenv("FACEBOOK_APP_ID")  # Facebook App ID
    FACEBOOK_APP_SECRET = os.getenv("FACEBOOK_APP_SECRET")  # Facebook App Secret
    FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")  # Facebook Access Token
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')  # بديل OpenAI
    MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', 'localhost:9000')
    MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'minioadmin')
    MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'minioadmin')

    # إعدادات الربح
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'pk_test_...')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'sk_test_...')

    # إعدادات التطبيق العامة
    DEBUG = os.getenv("DEBUG", "True") == "True"  # افتراضي: True
