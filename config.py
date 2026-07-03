import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Secret key used for sessions / CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-secret-key-in-production')

    # ---- MySQL Database Configuration ----
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'university_system')

    _database_url = os.environ.get('DATABASE_URL')
    if _database_url:
        if _database_url.startswith('postgres://'):
            _database_url = _database_url.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = _database_url
    else:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---- File Upload Configuration ----
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024  # 25 MB max upload size
    ALLOWED_EXTENSIONS = {
        'pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx',
        'txt', 'zip', 'rar', 'png', 'jpg', 'jpeg', 'gif', 'mp4'
    }

    # ---- Languages ----
    LANGUAGES = ['ar', 'en']
    DEFAULT_LANGUAGE = 'ar'
