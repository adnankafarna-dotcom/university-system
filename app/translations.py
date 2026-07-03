# -*- coding: utf-8 -*-
"""
نظام ترجمة بسيط قائم على قاموس بايثون (بدون الحاجة لأدوات gettext/babel الخارجية).
Simple dictionary-based translation system (no external gettext/babel tools required).

الاستخدام في القوالب Jinja: {{ t('login') }}
"""

TRANSLATIONS = {
    # ---------- عام / General ----------
    'app_name': {'ar': 'نظام الجامعة الذكي', 'en': 'Smart University System'},
    'home': {'ar': 'الرئيسية', 'en': 'Home'},
    'login': {'ar': 'تسجيل الدخول', 'en': 'Login'},
    'logout': {'ar': 'تسجيل الخروج', 'en': 'Logout'},
    'register': {'ar': 'إنشاء حساب', 'en': 'Register'},
    'username': {'ar': 'اسم المستخدم', 'en': 'Username'},
    'password': {'ar': 'كلمة المرور', 'en': 'Password'},
    'confirm_password': {'ar': 'تأكيد كلمة المرور', 'en': 'Confirm Password'},
    'full_name': {'ar': 'الاسم الكامل', 'en': 'Full Name'},
    'email': {'ar': 'البريد الإلكتروني', 'en': 'Email'},
    'role': {'ar': 'نوع الحساب', 'en': 'Account Type'},
    'teacher': {'ar': 'معلم', 'en': 'Teacher'},
    'student': {'ar': 'طالب', 'en': 'Student'},
    'submit': {'ar': 'إرسال', 'en': 'Submit'},
    'save': {'ar': 'حفظ', 'en': 'Save'},
    'cancel': {'ar': 'إلغاء', 'en': 'Cancel'},
    'welcome': {'ar': 'مرحباً', 'en': 'Welcome'},
    'dashboard': {'ar': 'لوحة التحكم', 'en': 'Dashboard'},
    'language': {'ar': 'اللغة', 'en': 'Language'},
    'back': {'ar': 'رجوع', 'en': 'Back'},
    'view': {'ar': 'عرض', 'en': 'View'},
    'edit': {'ar': 'تعديل', 'en': 'Edit'},
    'delete': {'ar': 'حذف', 'en': 'Delete'},
    'download': {'ar': 'تحميل', 'en': 'Download'},
    'created_at': {'ar': 'تاريخ الإنشاء', 'en': 'Created At'},
    'actions': {'ar': 'إجراءات', 'en': 'Actions'},
    'no_data': {'ar': 'لا توجد بيانات حالياً', 'en': 'No data available'},
    'success': {'ar': 'تمت العملية بنجاح', 'en': 'Operation successful'},
    'error': {'ar': 'حدث خطأ', 'en': 'An error occurred'},

    # ---------- الصفحة الرئيسية ----------
    'homepage_title': {'ar': 'منصة تعليمية متكاملة للمعلمين والطلاب', 'en': 'A Complete Learning Platform for Teachers and Students'},
    'homepage_subtitle': {'ar': 'إدارة المحاضرات والواجبات وتسليمها بسهولة', 'en': 'Manage lectures and assignments with ease'},
    'login_as_teacher': {'ar': 'دخول كمعلم', 'en': 'Login as Teacher'},
    'login_as_student': {'ar': 'دخول كطالب', 'en': 'Login as Student'},

    # ---------- المواد الدراسية ----------
    'course': {'ar': 'مادة دراسية', 'en': 'Course'},
    'courses': {'ar': 'المواد الدراسية', 'en': 'Courses'},
    'my_courses': {'ar': 'موادي الدراسية', 'en': 'My Courses'},
    'course_title': {'ar': 'اسم المادة', 'en': 'Course Title'},
    'course_code': {'ar': 'رمز المادة', 'en': 'Course Code'},
    'course_description': {'ar': 'وصف المادة', 'en': 'Course Description'},
    'add_course': {'ar': 'إضافة مادة جديدة', 'en': 'Add New Course'},
    'enroll': {'ar': 'انضمام للمادة', 'en': 'Enroll'},
    'enrolled': {'ar': 'مسجّل بالفعل', 'en': 'Already Enrolled'},
    'enrolled_students': {'ar': 'الطلاب المسجلون', 'en': 'Enrolled Students'},
    'available_courses': {'ar': 'المواد المتاحة للانضمام', 'en': 'Available Courses'},
    'enroll_with_code': {'ar': 'انضم بواسطة رمز المادة', 'en': 'Enroll using course code'},

    # ---------- المحاضرات ----------
    'lecture': {'ar': 'محاضرة', 'en': 'Lecture'},
    'lectures': {'ar': 'المحاضرات', 'en': 'Lectures'},
    'add_lecture': {'ar': 'إضافة محاضرة', 'en': 'Add Lecture'},
    'lecture_title': {'ar': 'عنوان المحاضرة', 'en': 'Lecture Title'},
    'lecture_content': {'ar': 'محتوى المحاضرة', 'en': 'Lecture Content'},
    'lecture_file': {'ar': 'ملف المحاضرة', 'en': 'Lecture File'},
    'video_url': {'ar': 'رابط فيديو (اختياري)', 'en': 'Video URL (optional)'},

    # ---------- الواجبات ----------
    'assignment': {'ar': 'واجب', 'en': 'Assignment'},
    'assignments': {'ar': 'الواجبات', 'en': 'Assignments'},
    'add_assignment': {'ar': 'إضافة واجب', 'en': 'Add Assignment'},
    'assignment_title': {'ar': 'عنوان الواجب', 'en': 'Assignment Title'},
    'assignment_description': {'ar': 'وصف الواجب', 'en': 'Assignment Description'},
    'due_date': {'ar': 'تاريخ التسليم', 'en': 'Due Date'},
    'max_grade': {'ar': 'الدرجة العظمى', 'en': 'Max Grade'},
    'attachment_file': {'ar': 'ملف مرفق (اختياري)', 'en': 'Attachment (optional)'},
    'submit_assignment': {'ar': 'تسليم الواجب', 'en': 'Submit Assignment'},
    'my_submission': {'ar': 'تسليمي', 'en': 'My Submission'},
    'submission_text': {'ar': 'نص الإجابة (اختياري)', 'en': 'Answer Text (optional)'},
    'submission_file': {'ar': 'ملف التسليم', 'en': 'Submission File'},
    'submitted_at': {'ar': 'وقت التسليم', 'en': 'Submitted At'},
    'submissions': {'ar': 'التسليمات', 'en': 'Submissions'},
    'view_submissions': {'ar': 'عرض التسليمات', 'en': 'View Submissions'},
    'grade': {'ar': 'الدرجة', 'en': 'Grade'},
    'feedback': {'ar': 'ملاحظات المعلم', 'en': 'Teacher Feedback'},
    'grade_submission': {'ar': 'تقييم التسليم', 'en': 'Grade Submission'},
    'not_submitted': {'ar': 'لم يتم التسليم بعد', 'en': 'Not submitted yet'},
    'not_graded': {'ar': 'لم يتم التقييم بعد', 'en': 'Not graded yet'},
    'status': {'ar': 'الحالة', 'en': 'Status'},
    'late': {'ar': 'متأخر', 'en': 'Late'},
    'on_time': {'ar': 'في الموعد', 'en': 'On Time'},

    # ---------- رسائل ----------
    'invalid_credentials': {'ar': 'اسم المستخدم أو كلمة المرور غير صحيحة', 'en': 'Invalid username or password'},
    'username_taken': {'ar': 'اسم المستخدم مستخدم بالفعل', 'en': 'Username already taken'},
    'email_taken': {'ar': 'البريد الإلكتروني مستخدم بالفعل', 'en': 'Email already registered'},
    'passwords_not_match': {'ar': 'كلمتا المرور غير متطابقتين', 'en': 'Passwords do not match'},
    'registered_successfully': {'ar': 'تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن', 'en': 'Account created successfully, you can now login'},
    'logged_out': {'ar': 'تم تسجيل الخروج بنجاح', 'en': 'Logged out successfully'},
    'course_created': {'ar': 'تم إنشاء المادة بنجاح', 'en': 'Course created successfully'},
    'lecture_added': {'ar': 'تمت إضافة المحاضرة بنجاح', 'en': 'Lecture added successfully'},
    'assignment_added': {'ar': 'تمت إضافة الواجب بنجاح', 'en': 'Assignment added successfully'},
    'enrolled_successfully': {'ar': 'تم الانضمام للمادة بنجاح', 'en': 'Enrolled in course successfully'},
    'already_enrolled': {'ar': 'أنت مسجل بالفعل في هذه المادة', 'en': 'You are already enrolled in this course'},
    'submission_success': {'ar': 'تم تسليم الواجب بنجاح', 'en': 'Assignment submitted successfully'},
    'grade_saved': {'ar': 'تم حفظ التقييم بنجاح', 'en': 'Grade saved successfully'},
    'not_authorized': {'ar': 'غير مصرح لك بهذا الإجراء', 'en': 'You are not authorized to perform this action'},
    'course_not_found': {'ar': 'المادة غير موجودة', 'en': 'Course not found'},
    'invalid_file_type': {'ar': 'نوع الملف غير مسموح', 'en': 'File type not allowed'},

    # ---------- لوحة المعلم ----------
    'teacher_dashboard': {'ar': 'لوحة تحكم المعلم', 'en': 'Teacher Dashboard'},
    'total_courses': {'ar': 'إجمالي المواد', 'en': 'Total Courses'},
    'total_students': {'ar': 'إجمالي الطلاب', 'en': 'Total Students'},
    'total_assignments': {'ar': 'إجمالي الواجبات', 'en': 'Total Assignments'},
    'pending_grading': {'ar': 'تسليمات بانتظار التقييم', 'en': 'Pending Grading'},

    # ---------- لوحة الطالب ----------
    'student_dashboard': {'ar': 'لوحة تحكم الطالب', 'en': 'Student Dashboard'},
    'upcoming_assignments': {'ar': 'واجبات قادمة', 'en': 'Upcoming Assignments'},
    'recent_lectures': {'ar': 'محاضرات حديثة', 'en': 'Recent Lectures'},
}


def t(key, lang='ar'):
    """إرجاع الترجمة المناسبة للمفتاح المعطى حسب اللغة الحالية."""
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    return entry.get(lang, entry.get('ar', key))
