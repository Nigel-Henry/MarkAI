# استخدم صورة Python 3.9-slim كقاعدة
FROM python:3.9-slim as base

# تعيين دليل العمل إلى /app
WORKDIR /app

# مرحلة التطوير
FROM base as development
# نسخ ملف المتطلبات إلى دليل العمل
COPY requirements.txt .
# تثبيت المتطلبات
RUN pip install -r requirements.txt
# تعيين الأمر الافتراضي لتشغيل Flask
CMD ["flask", "run", "--host=0.0.0.0"]

# مرحلة الإنتاج
FROM base as production
# نسخ جميع الملفات إلى دليل العمل
COPY . .
# تثبيت المتطلبات بدون استخدام ذاكرة التخزين المؤقت
RUN pip install --no-cache-dir -r requirements.txt
# تعيين الأمر الافتراضي لتشغيل Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
