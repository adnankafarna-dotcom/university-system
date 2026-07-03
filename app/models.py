from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    """
    جدول المستخدمين الموحد (معلم / طالب).
    Unified users table (teacher / student), differentiated by `role`.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'teacher' or 'student'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # علاقات
    courses_taught = db.relationship('Course', backref='teacher', lazy=True,
                                      foreign_keys='Course.teacher_id')
    enrollments = db.relationship('Enrollment', backref='student', lazy=True,
                                   foreign_keys='Enrollment.student_id')
    submissions = db.relationship('Submission', backref='student', lazy=True,
                                   foreign_keys='Submission.student_id')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_teacher(self):
        return self.role == 'teacher'

    def is_student(self):
        return self.role == 'student'

    def __repr__(self):
        return f'<User {self.username} ({self.role})>'


class Course(db.Model):
    """مادة دراسية ينشئها المعلم."""
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    lectures = db.relationship('Lecture', backref='course', lazy=True,
                                cascade='all, delete-orphan')
    assignments = db.relationship('Assignment', backref='course', lazy=True,
                                   cascade='all, delete-orphan')
    enrollments = db.relationship('Enrollment', backref='course', lazy=True,
                                   cascade='all, delete-orphan')

    def student_count(self):
        return len(self.enrollments)

    def __repr__(self):
        return f'<Course {self.code} - {self.title}>'


class Enrollment(db.Model):
    """تسجيل طالب في مادة دراسية."""
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'course_id', name='uq_student_course'),
    )


class Lecture(db.Model):
    """محاضرة يرفعها المعلم ضمن مادة دراسية."""
    __tablename__ = 'lectures'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    video_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Lecture {self.title}>'


class Assignment(db.Model):
    """واجب ينشئه المعلم ضمن مادة دراسية."""
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    max_grade = db.Column(db.Float, default=100.0)
    file_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    submissions = db.relationship('Submission', backref='assignment', lazy=True,
                                   cascade='all, delete-orphan')

    def submission_for(self, student_id):
        return Submission.query.filter_by(
            assignment_id=self.id, student_id=student_id
        ).first()

    def __repr__(self):
        return f'<Assignment {self.title}>'


class Submission(db.Model):
    """تسليم طالب لواجب معين."""
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text_answer = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Float, nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    graded_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint('assignment_id', 'student_id', name='uq_assignment_student'),
    )

    def is_graded(self):
        return self.grade is not None

    def __repr__(self):
        return f'<Submission by user {self.student_id} for assignment {self.assignment_id}>'
