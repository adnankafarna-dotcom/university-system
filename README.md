# نظام الجامعة الذكي | Smart University System

نظام ويب متكامل لإدارة العملية التعليمية باستخدام **Python (Flask)** و **MySQL**، يدعم دخولاً منفصلاً للمعلمين والطلاب، مع دعم كامل للغتين **العربية (RTL)** و **الإنجليزية**.

A full-featured web-based learning management system built with **Flask** and **MySQL**, with separate login for teachers and students, and full bilingual support (Arabic RTL / English).

---

## المزايا الرئيسية | Key Features

- 🔐 نظام مصادقة منفصل للمعلم والطالب (Role-based authentication)
- 📚 إنشاء وإدارة المواد الدراسية (Courses) من قِبل المعلم، بكود انضمام فريد
- 🎥 رفع المحاضرات (ملفات + روابط فيديو)
- 📝 إنشاء الواجبات مع تاريخ تسليم ودرجة عظمى
- 📤 تسليم الطلاب لواجباتهم (نص + ملف مرفق)
- ✅ تقييم المعلم للتسليمات مع ملاحظات
- 🌐 تبديل فوري بين العربية والإنجليزية مع دعم RTL كامل
- 🎨 واجهة عصرية باستخدام Bootstrap 5

---

## هيكل المشروع | Project Structure

```
university_system/
├── app/
│   ├── __init__.py        # Application factory
│   ├── models.py          # SQLAlchemy models
│   ├── forms.py            # WTForms
│   ├── utils.py             # Helper functions
│   ├── translations.py      # AR/EN dictionary-based i18n
│   ├── routes/
│   │   ├── main.py           # Home page + language switch
│   │   ├── auth.py           # Login / Register / Logout
│   │   ├── teacher.py        # Teacher features
│   │   └── student.py        # Student features
│   ├── templates/            # Jinja2 HTML templates
│   └── static/
│       ├── css/
│       └── uploads/          # Uploaded files (lectures/assignments/submissions)
├── config.py
├── run.py
├── init_db.py
├── requirements.txt
└── .env.example
```

---

## خطوات التثبيت | Setup Instructions

### 1) إنشاء بيئة افتراضية | Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # على Linux/Mac
venv\Scripts\activate         # على Windows
```

### 2) تثبيت المتطلبات | Install dependencies
```bash
pip install -r requirements.txt
```

### 3) إعداد قاعدة بيانات MySQL | Set up MySQL database
تأكد أن MySQL يعمل على جهازك، ثم أنشئ قاعدة البيانات:
```sql
CREATE DATABASE university_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4) إعداد ملف البيئة | Configure environment variables
```bash
cp .env.example .env
```
ثم عدّل القيم داخل `.env` (اسم المستخدم، كلمة المرور، اسم قاعدة البيانات...).

### 5) إنشاء الجداول | Create database tables
```bash
python init_db.py
```
لإضافة بيانات تجريبية (معلم + طالب + مادة جاهزة للاختبار):
```bash
python init_db.py --seed
```
بيانات الدخول التجريبية:
- المعلم: `teacher1` / `teacher123`
- الطالب: `student1` / `student123`
- كود المادة: `CS101`

### 6) تشغيل التطبيق | Run the application
```bash
python run.py
```
ثم افتح المتصفح على: `http://localhost:5000`

---

## ملاحظات مهمة | Important Notes

- **الترجمة**: النظام يستخدم قاموس بايثون بسيط (`app/translations.py`) بدل أدوات gettext المعقدة، لذا يمكنك إضافة أي عبارة جديدة بسهولة بإضافة سطر بالقاموس.
- **رفع الملفات**: يتم حفظ الملفات في `app/static/uploads/` مع أسماء فريدة (UUID) لتفادي التعارض.
- **الأمان**: كلمات المرور مشفّرة (Werkzeug hashing)، وكل الفورمات محمية بـ CSRF Token.
- **قابلية التوسع**: يمكنك بسهولة إضافة: نظام إشعارات، شات بين المعلم والطالب، تقارير Excel/PDF، اختبارات إلكترونية (Quizzes)... الخ.

---

## أفكار للتطوير المستقبلي | Future Enhancements

- [ ] لوحة تحكم إدارية (Admin) لإدارة المستخدمين والمواد
- [ ] نظام إشعارات بالبريد الإلكتروني عند إضافة واجب/محاضرة جديدة
- [ ] اختبارات إلكترونية (Quizzes) بتصحيح تلقائي
- [ ] تقارير وإحصائيات أداء الطلاب (Excel/PDF Export)
- [ ] دردشة مباشرة بين المعلم والطالب
