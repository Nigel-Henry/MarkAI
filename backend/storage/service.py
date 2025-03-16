# backend/app/features/storage/service.py
import os
from werkzeug.utils import secure_filename

class FileStorage:
    UPLOAD_FOLDER = 'uploads'

    def __init__(self):
        # تأكد من وجود مجلد التحميل
        if not os.path.exists(self.UPLOAD_FOLDER):
            os.makedirs(self.UPLOAD_FOLDER)

    def save(self, file):
        """
        حفظ الملف في مجلد التحميل بعد تأمين اسمه.
        
        Args:
            file (werkzeug.datastructures.FileStorage): الملف المراد حفظه.
        
        Returns:
            str: اسم الملف المحفوظ.
        """
        filename = secure_filename(file.filename)
        file_path = os.path.join(self.UPLOAD_FOLDER, filename)
        file.save(file_path)
        return filename