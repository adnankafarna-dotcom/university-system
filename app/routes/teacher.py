import uuid
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app import db
from app.models import Course, Lecture, Assignment, Submission
from app.forms import CourseForm, LectureForm, AssignmentForm, GradeForm
from app.utils import role_required, save_uploaded_file

teacher_bp = Blueprint('teacher', __name__)


def _get_owned_course_or_404(course_id):
    course = Course.query.get_or_404(course_id)
    if course.teacher_id != current_user.id:
        abort(403)
    return course


@teacher_bp.route('/dashboard')
@login_required
@role_required('teacher')
def dashboard():
    courses = Course.query.filter_by(teacher_id=current_user.id).order_by(
        Course.created_at.desc()
    ).all()

    total_students = sum(c.student_count() for c in courses)
    total_assignments = sum(len(c.assignments) for c in courses)
    pending_grading = (
        db.session.query(Submission)
        .join(Assignment, Submission.assignment_id == Assignment.id)
        .join(Course, Assignment.course_id == Course.id)
        .filter(Course.teacher_id == current_user.id, Submission.grade.is_(None))
        .count()
    )

    return render_template(
        'teacher/dashboard.html',
        courses=courses,
        total_students=total_students,
        total_assignments=total_assignments,
        pending_grading=pending_grading,
    )


@teacher_bp.route('/course/new', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def new_course():
    form = CourseForm()
    if form.validate_on_submit():
        code = form.code.data.strip().upper()
        if Course.query.filter_by(code=code).first():
            code = f"{code}-{uuid.uuid4().hex[:4].upper()}"

        course = Course(
            title=form.title.data,
            code=code,
            description=form.description.data,
            teacher_id=current_user.id,
        )
        db.session.add(course)
        db.session.commit()
        flash('course_created', 'success')
        return redirect(url_for('teacher.course_detail', course_id=course.id))

    return render_template('teacher/course_form.html', form=form)


@teacher_bp.route('/course/<int:course_id>')
@login_required
@role_required('teacher')
def course_detail(course_id):
    course = _get_owned_course_or_404(course_id)
    return render_template('teacher/course_detail.html', course=course)


@teacher_bp.route('/course/<int:course_id>/lecture/new', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def new_lecture(course_id):
    course = _get_owned_course_or_404(course_id)
    form = LectureForm()
    if form.validate_on_submit():
        file_path = save_uploaded_file(form.file.data, 'lectures')
        lecture = Lecture(
            course_id=course.id,
            title=form.title.data,
            content=form.content.data,
            video_url=form.video_url.data,
            file_path=file_path,
        )
        db.session.add(lecture)
        db.session.commit()
        flash('lecture_added', 'success')
        return redirect(url_for('teacher.course_detail', course_id=course.id))

    return render_template('teacher/lecture_form.html', form=form, course=course)


@teacher_bp.route('/course/<int:course_id>/assignment/new', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def new_assignment(course_id):
    course = _get_owned_course_or_404(course_id)
    form = AssignmentForm()
    if form.validate_on_submit():
        file_path = save_uploaded_file(form.file.data, 'assignments')
        assignment = Assignment(
            course_id=course.id,
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            max_grade=form.max_grade.data or 100.0,
            file_path=file_path,
        )
        db.session.add(assignment)
        db.session.commit()
        flash('assignment_added', 'success')
        return redirect(url_for('teacher.course_detail', course_id=course.id))

    return render_template('teacher/assignment_form.html', form=form, course=course)


@teacher_bp.route('/assignment/<int:assignment_id>/submissions')
@login_required
@role_required('teacher')
def view_submissions(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    course = _get_owned_course_or_404(assignment.course_id)
    submissions = Submission.query.filter_by(assignment_id=assignment.id).order_by(
        Submission.submitted_at.desc()
    ).all()
    return render_template(
        'teacher/submissions.html',
        assignment=assignment, course=course, submissions=submissions
    )


@teacher_bp.route('/submission/<int:submission_id>/grade', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def grade_submission(submission_id):
    submission = Submission.query.get_or_404(submission_id)
    assignment = submission.assignment
    course = _get_owned_course_or_404(assignment.course_id)

    form = GradeForm(obj=submission)
    if form.validate_on_submit():
        submission.grade = form.grade.data
        submission.feedback = form.feedback.data
        submission.graded_at = datetime.utcnow()
        db.session.commit()
        flash('grade_saved', 'success')
        return redirect(url_for('teacher.view_submissions', assignment_id=assignment.id))

    return render_template(
        'teacher/grade_form.html', form=form, submission=submission,
        assignment=assignment, course=course
    )
