from django.http import JsonResponse
from django.shortcuts import render
from .validators import validate_file_extension,validate_file_size
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
from .utils import read_uploaded_file
# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def upload_resume(request):
    if request.method == 'POST' and request.FILES.get("file"):
        file : UploadedFile = request.FILES['file']
        try:
            ext:str = validate_file_extension(file)
            validate_file_extension(file)
            validate_file_size(file)
            file_content = read_uploaded_file(file , ext)
            print("file=",file_content)
        except ValidationError as err: 
            return JsonResponse({"error": str(err.message)})
    return JsonResponse({"error":"Invalid Request"},status=400)    