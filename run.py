from app import create_app, db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    from app.models import User, Course, Enrollment, Lecture, Assignment, Submission
    return dict(
        db=db, User=User, Course=Course, Enrollment=Enrollment,
        Lecture=Lecture, Assignment=Assignment, Submission=Submission
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
