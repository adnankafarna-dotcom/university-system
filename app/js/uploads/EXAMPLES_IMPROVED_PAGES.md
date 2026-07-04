# 🎨 أمثلة صفحات محسّنة | Improved Pages Examples

---

## 📝 صفحة تسجيل الدخول محسّنة

```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center min-vh-100 align-items-center">
    <div class="col-md-5 col-lg-4">
        <!-- Hero Section -->
        <div class="hero mb-5 text-center">
            <i class="bi bi-mortarboard-fill" style="font-size: 4rem;"></i>
            <h1 class="mt-3">{{ t('app_name') }}</h1>
            <p class="lead text-white-50">منصة تعليمية ذكية متكاملة</p>
        </div>

        <!-- Login Card -->
        <div class="card shadow-lg">
            <div class="card-header text-center py-4">
                <h4 class="mb-0">
                    <i class="bi bi-box-arrow-in-right me-2"></i>
                    {{ t('login') }}
                </h4>
            </div>

            <div class="card-body p-4">
                <form method="POST" class="needs-validation" novalidate>
                    {{ form.hidden_tag() }}

                    <!-- Username Field -->
                    <div class="mb-3">
                        {{ form.username.label(class="form-label") }}
                        {% if form.username.errors %}
                            {{ form.username(class="form-control is-invalid") }}
                            <div class="invalid-feedback d-block">
                                {% for error in form.username.errors %}
                                    <i class="bi bi-exclamation-circle me-1"></i>{{ error }}
                                {% endfor %}
                            </div>
                        {% else %}
                            {{ form.username(class="form-control", placeholder=t('username')) }}
                        {% endif %}
                    </div>

                    <!-- Password Field -->
                    <div class="mb-3">
                        {{ form.password.label(class="form-label") }}
                        {% if form.password.errors %}
                            {{ form.password(class="form-control is-invalid") }}
                            <div class="invalid-feedback d-block">
                                {% for error in form.password.errors %}
                                    <i class="bi bi-exclamation-circle me-1"></i>{{ error }}
                                {% endfor %}
                            </div>
                        {% else %}
                            {{ form.password(class="form-control", placeholder=t('password')) }}
                        {% endif %}
                    </div>

                    <!-- Submit Button -->
                    <button type="submit" class="btn btn-primary btn-lg w-100 fw-bold">
                        <i class="bi bi-box-arrow-in-right me-2"></i>
                        {{ t('login') }}
                    </button>
                </form>
            </div>

            <div class="card-footer text-center py-3">
                <p class="mb-0">
                    ليس لديك حساب؟
                    <a href="{{ url_for('auth.register') }}" class="fw-bold">
                        {{ t('register') }}
                    </a>
                </p>
            </div>
        </div>

        <!-- Demo Credentials -->
        <div class="alert alert-info mt-4 text-center">
            <i class="bi bi-info-circle me-2"></i>
            <small>
                <strong>بيانات تجريبية:</strong><br>
                اسم المستخدم: teacher1<br>
                كلمة المرور: teacher123
            </small>
        </div>
    </div>
</div>

<style>
.min-vh-100 {
    min-height: 100vh;
}
</style>
{% endblock %}
```

---

## 📊 صفحة Dashboard محسّنة

```html
{% extends 'base.html' %}

{% block content %}
<!-- Welcome Banner -->
<div class="hero mb-5">
    <div class="hero-content">
        <h1>
            <i class="bi bi-hand-thumbs-up-fill me-3"></i>
            مرحباً {{ current_user.full_name }}
        </h1>
        <p class="lead text-white-50 mb-0">
            أهلاً وسهلاً في نظام الجامعة الذكي
        </p>
    </div>
</div>

<!-- Statistics Cards -->
<div class="row mb-5">
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="dashboard-card">
            <div class="dashboard-card-icon">
                <i class="bi bi-book-fill"></i>
            </div>
            <h5>المواد الدراسية</h5>
            <p class="mb-0">
                <strong class="text-primary" style="font-size: 1.5rem;">
                    {{ courses_count | default(0) }}
                </strong>
            </p>
        </div>
    </div>

    <div class="col-md-6 col-lg-3 mb-4">
        <div class="dashboard-card">
            <div class="dashboard-card-icon">
                <i class="bi bi-file-earmark-text-fill"></i>
            </div>
            <h5>المحاضرات</h5>
            <p class="mb-0">
                <strong class="text-primary" style="font-size: 1.5rem;">
                    {{ lectures_count | default(0) }}
                </strong>
            </p>
        </div>
    </div>

    <div class="col-md-6 col-lg-3 mb-4">
        <div class="dashboard-card">
            <div class="dashboard-card-icon">
                <i class="bi bi-checkmark-circle-fill"></i>
            </div>
            <h5>المهام المكتملة</h5>
            <p class="mb-0">
                <strong class="text-success" style="font-size: 1.5rem;">
                    {{ completed_tasks | default(0) }}
                </strong>
            </p>
        </div>
    </div>

    <div class="col-md-6 col-lg-3 mb-4">
        <div class="dashboard-card">
            <div class="dashboard-card-icon">
                <i class="bi bi-hourglass-split"></i>
            </div>
            <h5>المهام المتبقية</h5>
            <p class="mb-0">
                <strong class="text-warning" style="font-size: 1.5rem;">
                    {{ pending_tasks | default(0) }}
                </strong>
            </p>
        </div>
    </div>
</div>

<!-- Courses Table -->
<div class="card">
    <div class="card-header d-flex align-items-center gap-2">
        <i class="bi bi-book-fill"></i>
        <h5 class="mb-0">المواد الدراسية</h5>
    </div>
    <div class="card-body">
        {% if courses %}
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th onclick="sortTable(0)" style="cursor: pointer;">
                                الكود <i class="bi bi-arrow-down-up"></i>
                            </th>
                            <th>المادة</th>
                            <th>المعلم</th>
                            <th>الإجراءات</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for course in courses %}
                        <tr>
                            <td>
                                <span class="badge bg-primary">{{ course.code }}</span>
                            </td>
                            <td>{{ course.title }}</td>
                            <td>{{ course.teacher.full_name }}</td>
                            <td>
                                <a href="{{ url_for('student.course_detail', course_id=course.id) }}" 
                                   class="btn btn-sm btn-outline-primary">
                                    <i class="bi bi-eye-fill"></i> عرض
                                </a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="alert alert-info">
                <i class="bi bi-info-circle me-2"></i>
                لا توجد مواد دراسية حالياً
            </div>
        {% endif %}
    </div>
</div>

{% endblock %}
```

---

## 📋 نموذج إنشاء محسّن

```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-lg-8">
        <div class="card shadow">
            <div class="card-header">
                <h4 class="mb-0">
                    <i class="bi bi-plus-circle-fill me-2"></i>
                    إنشاء مادة دراسية جديدة
                </h4>
            </div>

            <div class="card-body p-5">
                <form method="POST" class="needs-validation" novalidate>
                    {{ form.hidden_tag() }}

                    <!-- Course Title -->
                    <div class="mb-4">
                        {{ form.title.label(class="form-label") }}
                        {% if form.title.errors %}
                            {{ form.title(class="form-control is-invalid") }}
                            <div class="invalid-feedback d-block">
                                {% for error in form.title.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% else %}
                            {{ form.title(class="form-control", placeholder="مثال: مقدمة في البرمجة") }}
                        {% endif %}
                    </div>

                    <!-- Course Code -->
                    <div class="mb-4">
                        {{ form.code.label(class="form-label") }}
                        {% if form.code.errors %}
                            {{ form.code(class="form-control is-invalid") }}
                            <div class="invalid-feedback d-block">
                                {% for error in form.code.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% else %}
                            {{ form.code(class="form-control", placeholder="مثال: CS101") }}
                        {% endif %}
                    </div>

                    <!-- Course Description -->
                    <div class="mb-4">
                        {{ form.description.label(class="form-label") }}
                        {% if form.description.errors %}
                            {{ form.description(class="form-control is-invalid", rows="4") }}
                            <div class="invalid-feedback d-block">
                                {% for error in form.description.errors %}
                                    {{ error }}
                                {% endfor %}
                            </div>
                        {% else %}
                            {{ form.description(class="form-control", rows="4", placeholder="وصف المادة الدراسية...") }}
                        {% endif %}
                    </div>

                    <!-- Submit Buttons -->
                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-primary btn-lg flex-grow-1">
                            <i class="bi bi-check-circle me-2"></i>
                            {{ t('save') }}
                        </button>
                        <a href="{{ url_for('teacher.dashboard') }}" class="btn btn-outline-secondary btn-lg">
                            <i class="bi bi-x-circle me-2"></i>
                            {{ t('cancel') }}
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
    // Form Validation
    (function() {
        'use strict';
        const forms = document.querySelectorAll('.needs-validation');
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    })();
</script>
{% endblock %}
```

---

## 🗂️ صفحة قائمة محسّنة

```html
{% extends 'base.html' %}

{% block content %}
<!-- Header with Search -->
<div class="row mb-4">
    <div class="col-md-6">
        <h2>
            <i class="bi bi-list-ul me-2"></i>
            قائمة الطلاب
        </h2>
    </div>
    <div class="col-md-6">
        <input type="text" class="form-control" id="searchInput" 
               placeholder="ابحث عن طالب..."
               onkeyup="filterTable(this.value)">
    </div>
</div>

<!-- Action Buttons -->
<div class="mb-4">
    <a href="{{ url_for('teacher.add_student') }}" class="btn btn-primary">
        <i class="bi bi-plus-circle me-2"></i>
        إضافة طالب جديد
    </a>
    <button onclick="exportTableToCSV('studentTable', 'students.csv')" class="btn btn-outline-success">
        <i class="bi bi-download me-2"></i>
        تصدير CSV
    </button>
</div>

<!-- Table -->
<div class="card">
    <div class="table-responsive">
        <table class="table table-hover mb-0" id="studentTable">
            <thead>
                <tr>
                    <th onclick="sortTable(0)" style="cursor: pointer;">
                        الرقم الطالب <i class="bi bi-arrow-down-up"></i>
                    </th>
                    <th onclick="sortTable(1)" style="cursor: pointer;">
                        الاسم <i class="bi bi-arrow-down-up"></i>
                    </th>
                    <th>البريد الإلكتروني</th>
                    <th>الحالة</th>
                    <th>الإجراءات</th>
                </tr>
            </thead>
            <tbody>
                {% for student in students %}
                <tr>
                    <td>
                        <span class="badge bg-info">{{ student.id }}</span>
                    </td>
                    <td>
                        <strong>{{ student.full_name }}</strong>
                    </td>
                    <td>
                        <a href="mailto:{{ student.email }}">{{ student.email }}</a>
                    </td>
                    <td>
                        <span class="badge bg-success">نشط</span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                            <a href="{{ url_for('teacher.student_detail', student_id=student.id) }}" 
                               class="btn btn-sm btn-outline-primary" title="عرض">
                                <i class="bi bi-eye"></i>
                            </a>
                            <a href="{{ url_for('teacher.edit_student', student_id=student.id) }}" 
                               class="btn btn-sm btn-outline-warning" title="تعديل">
                                <i class="bi bi-pencil"></i>
                            </a>
                            <button class="btn btn-sm btn-outline-danger" 
                                    onclick="if(confirm('هل متأكد؟')) location.href='{{ url_for('teacher.delete_student', student_id=student.id) }}'">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<script>
    // Include script.js functions for filtering and exporting
</script>
{% endblock %}
```

---

## ✅ الميزات المستخدمة

✅ Dark Mode Support
✅ Responsive Design
✅ Icons جميلة
✅ Animations سلسة
✅ Form Validation
✅ Table Filtering
✅ Export CSV
✅ Alerts محسّنة

---

## 🚀 نصائح الاستخدام

1. **انسخ الكود** من الأمثلة أعلاه
2. **عدّل** الأجزاء اللي تحتاجها
3. **اختبر** على الموقع المحلي
4. **ارفع** التغييرات

---

**استمتع بتصميمك الاحترافي! 🎉**
