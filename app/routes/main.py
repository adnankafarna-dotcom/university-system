from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_teacher():
            return redirect(url_for('teacher.dashboard'))
        return redirect(url_for('student.dashboard'))
    return render_template('index.html')


@main_bp.route('/set_language/<lang>')
def set_language(lang):
    if lang in ('ar', 'en'):
        session['lang'] = lang
    return redirect(request.referrer or url_for('main.index'))
