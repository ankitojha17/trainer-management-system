import os
from .exceptions import FileValidationError

def validate_resource_file(file_obj):
    ext = os.path.splitext(file_obj.name)[1].lower()
    if ext not in ['.pdf', '.docx']:
        raise FileValidationError("Invalid file extension. Only .pdf and .docx are supported.")

    if file_obj.size > 2 * 1024 * 1024:
        raise FileValidationError("File size exceeds the 2MB limit.")