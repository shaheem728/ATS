from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def upload_resume(request):
    if request.method == 'POST' and request.FILES.get("file"):
        ...
    return JsonResponse({"error":"Invalid Request"},status=400)    