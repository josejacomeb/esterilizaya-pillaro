from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inscripcion/index.html')

