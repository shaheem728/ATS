from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
import os

VALID_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".doc",

]

def validate_file_extension(file_object:UploadedFile):
    file_extension:str = os.path.splitext(file_object.name)[1].lower()
    if file_extension.lower() not in VALID_EXTENSIONS:
        raise ValidationError(f"Only PDF, DOCX and DOC files are allowed.{file_extension} detected")
    
def validate_file_size(file_object:UploadedFile):   
    MAX_UPLOAD_SIZE = 2_096_152 
    if file_object.size > MAX_UPLOAD_SIZE:
        raise ValidationError("Max file size is 2MB")
    