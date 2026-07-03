from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app import db
from app.models import Course, Enrollment, Assignment, Submission
from app.forms import EnrollForm, SubmissionForm
from app.utils import role_required, save_uploaded_file

student_bp = Blueprint('student', __name__)


@student_bp.route('/dashboard')
@login_required
@role_required('student')
def dashboard():
    enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
    courses = [e.course for e in enrollments]

    upcoming_assignments = (
        Assignment.query
        .filter(Assignment.course_id.in_([c.id for c in courses]))
        .order_by(Assignment.due_date.asc())
        .limit(10)
        .all()
    ) if courses else []

    all_courses = Course.query.order_by(Course.created_at.desc()).all()
    enrolled_ids = {c.id for c in courses}
    available_courses = [c for c in all_courses if c.id not in enrolled_ids]

    enroll_form = EnrollForm()

    return render_template(
        'student/dashboard.html',
        courses=courses,
        upcoming_assignments=upcoming_assignments,
        available_courses=available_courses,
        enroll_form=enroll_form,
    )


@student_bp.route('/enroll', methods=['POST'])
@login_required
@role_required('student')
def enroll():
    form = EnrollForm()
    if form.validate_on_submit():
        course = Course.query.filter_by(code=form.code.data.strip().upper()).first()
        if not course:
            flash('course_not_found', 'danger')
            return redirect(url_for('student.dashboard'))

        existing = Enrollment.query.filter_by(
            student_id=current_user.id, course_id=course.id
        ).first()
        if existing:
            flash('already_enrolled', 'warning')
        else:
            db.session.add(Enrollment(student_id=current_user.id, course_id=course.id))
            db.session.commit()
            flash('enrolled_successfully', 'success')

    return redirect(url_for('student.dashboard'))


def _get_enrolled_course_or_404(course_id):
    course = Course.query.get_or_404(course_id)
    enrolled = Enrollment.query.filter_by(
        student_id=current_user.id, course_id=course.id
    ).first()
    if not enrolled:
        abort(403)
    return course


@student_bp.route('/course/<int:course_id>')
@login_required
@role_required('student')
def course_detail(course_id):
    course = _get_enrolled_course_or_404(course_id)
    return render_template('student/course_detail.html', course=course)


@student_bp.route('/assignment/<int:assignment_id>/submit', methods=['GET', 'POST'])
@login_required
@role_required('student')
def submit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    course = _get_enrolled_course_or_404(assignment.course_id)

    existing_submission = assignment.submission_for(current_user.id)
    form = SubmissionForm(obj=existing_submission)

    if form.validate_on_submit():
        file_path = save_uploaded_file(form.file.data, 'submissions')

        if existing_submission:
            existing_submission.text_answer = form.text_answer.data
            if file_path:
                existing_submission.file_path = file_path
            existing_submission.submitted_at = datetime.utcnow()
        else:
            submission = Submission(
                assignment_id=assignment.id,
                student_id=current_user.id,
                text_answer=form.text_answer.data,
                file_path=file_path,
            )
            db.session.add(submission)

        db.session.commit()
        flash('submission_success', 'success')
        return redirect(url_for('student.course_detail', course_id=course.id))

    return render_template(
        'student/submit_assignment.html',
        form=form, assignment=assignment, course=course,
        existing_submission=existing_submission,
    )
