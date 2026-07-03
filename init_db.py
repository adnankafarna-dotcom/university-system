"""
سكربت لإنشاء جداول قاعدة البيانات، مع خيار إضافة بيانات تجريبية.
Script to create database tables, with an option to seed demo data.

الاستخدام / Usage:
    python init_db.py          # إنشاء الجداول فقط
    python init_db.py --seed   # إنشاء الجداول + بيانات تجريبية (معلم + طالب + مادة)
"""
import sys
from app import create_app, db
from app.models import User, Course, Enrollment

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ تم إنشاء الجداول بنجاح / Tables created successfully.")

    if '--seed' in sys.argv:
        if not User.query.filter_by(username='teacher1').first():
            teacher = User(
                username='teacher1', email='teacher1@example.com',
                full_name='أ. أحمد المعلم', role='teacher'
            )
            teacher.set_password('teacher123')
            db.session.add(teacher)

            student = User(
                username='student1', email='student1@example.com',
                full_name='محمد الطالب', role='student'
            )
            student.set_password('student123')
            db.session.add(student)
            db.session.commit()

            course = Course(
                title='Introduction to Programming',
                code='CS101',
                description='مقدمة في البرمجة باستخدام بايثون',
                teacher_id=teacher.id,
            )
            db.session.add(course)
            db.session.commit()

            db.session.add(Enrollment(student_id=student.id, course_id=course.id))
            db.session.commit()

            print("✅ تمت إضافة بيانات تجريبية / Demo data seeded:")
            print("   Teacher -> username: teacher1 | password: teacher123")
            print("   Student -> username: student1 | password: student123")
            print("   Course  -> code: CS101")
        else:
            print("ℹ️ البيانات التجريبية موجودة بالفعل / Demo data already exists.")
