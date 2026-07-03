import os
import uuid
from functools import wraps
from flask import current_app, abort
from flask_login import current_user
from werkzeug.utils import secure_filename


def role_required(role):
    """ديكوريتور يسمح فقط للمستخدمين بدور معين (teacher/student) بالوصول للراوت."""
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator


def save_uploaded_file(file_storage, subfolder):
    """
    يحفظ ملفاً مرفوعاً باسم فريد داخل مجلد فرعي معين تحت مجلد uploads.
    يرجع المسار النسبي المخزَّن في قاعدة البيانات، أو None إن لم يوجد ملف.
    """
    if not file_storage or file_storage.filename == '':
        return None

    filename = secure_filename(file_storage.filename)
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
    unique_name = f"{uuid.uuid4().hex}.{ext}" if ext else uuid.uuid4().hex

    folder = os.path.join(current_app.config['UPLOAD_FOLDER'], subfolder)
    os.makedirs(folder, exist_ok=True)
    full_path = os.path.join(folder, unique_name)
    file_storage.save(full_path)

    # المسار النسبي الذي سيُستخدم مع url_for('static', filename=...)
    return f"uploads/{subfolder}/{unique_name}"
