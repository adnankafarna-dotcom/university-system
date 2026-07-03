import os
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

from config import Config
from app.translations import t, TRANSLATIONS

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # تأكد من وجود مجلدات الرفع
    for sub in ('lectures', 'assignments', 'submissions'):
        os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], sub), exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ---- تحديد اللغة الحالية لكل طلب ----
    @app.before_request
    def set_language():
        if 'lang' not in session:
            session['lang'] = app.config['DEFAULT_LANGUAGE']

    # ---- إتاحة دالة الترجمة t() ومتغير اللغة داخل القوالب ----
    @app.context_processor
    def inject_translation():
        lang = session.get('lang', app.config['DEFAULT_LANGUAGE'])
        return {
            't': lambda key: t(key, lang),
            'current_lang': lang,
            'is_rtl': lang == 'ar',
        }

    # ---- تسجيل البلوبرنتس (Blueprints) ----
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.teacher import teacher_bp
    from app.routes.student import student_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(teacher_bp, url_prefix='/teacher')
    app.register_blueprint(student_bp, url_prefix='/student')

    return app
