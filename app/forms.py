from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, PasswordField, SelectField, TextAreaField,
    FloatField, DateTimeField, SubmitField
)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('password', validators=[DataRequired()])
    role = SelectField('role', choices=[('teacher', 'Teacher'), ('student', 'Student')],
                        validators=[DataRequired()])
    submit = SubmitField('login')


class RegisterForm(FlaskForm):
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=3, max=150)])
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('email', validators=[DataRequired(), Email()])
    role = SelectField('role', choices=[('teacher', 'Teacher'), ('student', 'Student')],
                        validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        'confirm_password',
        validators=[DataRequired(), EqualTo('password', message='passwords_not_match')]
    )
    submit = SubmitField('register')


class CourseForm(FlaskForm):
    title = StringField('course_title', validators=[DataRequired(), Length(max=150)])
    code = StringField('course_code', validators=[DataRequired(), Length(max=20)])
    description = TextAreaField('course_description', validators=[Optional()])
    submit = SubmitField('save')


class EnrollForm(FlaskForm):
    code = StringField('course_code', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('enroll')


ALLOWED_DOC_EXT = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx',
                    'txt', 'zip', 'rar', 'png', 'jpg', 'jpeg', 'gif', 'mp4']


class LectureForm(FlaskForm):
    title = StringField('lecture_title', validators=[DataRequired(), Length(max=200)])
    content = TextAreaField('lecture_content', validators=[Optional()])
    video_url = StringField('video_url', validators=[Optional(), Length(max=255)])
    file = FileField('lecture_file', validators=[
        Optional(), FileAllowed(ALLOWED_DOC_EXT, 'invalid_file_type')
    ])
    submit = SubmitField('save')


class AssignmentForm(FlaskForm):
    title = StringField('assignment_title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('assignment_description', validators=[Optional()])
    due_date = DateTimeField('due_date', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    max_grade = FloatField('max_grade', validators=[Optional()], default=100.0)
    file = FileField('attachment_file', validators=[
        Optional(), FileAllowed(ALLOWED_DOC_EXT, 'invalid_file_type')
    ])
    submit = SubmitField('save')


class SubmissionForm(FlaskForm):
    text_answer = TextAreaField('submission_text', validators=[Optional()])
    file = FileField('submission_file', validators=[
        Optional(), FileAllowed(ALLOWED_DOC_EXT, 'invalid_file_type')
    ])
    submit = SubmitField('submit_assignment')


class GradeForm(FlaskForm):
    grade = FloatField('grade', validators=[DataRequired()])
    feedback = TextAreaField('feedback', validators=[Optional()])
    submit = SubmitField('save')
