from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.models import User
from app.forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    # تحديد الدور مسبقاً إن جاء عبر الرابط: /auth/login?role=teacher
    default_role = request.args.get('role')
    if default_role in ('teacher', 'student') and request.method == 'GET':
        form.role.data = default_role

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, role=form.role.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        flash('invalid_credentials', 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('username_taken', 'danger')
            return render_template('auth/register.html', form=form)
        if User.query.filter_by(email=form.email.data).first():
            flash('email_taken', 'danger')
            return render_template('auth/register.html', form=form)

        user = User(
            full_name=form.full_name.data,
            username=form.username.data,
            email=form.email.data,
            role=form.role.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('registered_successfully', 'success')
        return redirect(url_for('auth.login', role=user.role))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logged_out', 'success')
    return redirect(url_for('main.index'))
