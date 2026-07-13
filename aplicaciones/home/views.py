from django.shortcuts import render
from django.views.generic import TemplateView
from .estudiantes import estudiantes

# Create your views here.
def home(request):
    return render(request, 'home.html', {'estudiantes': estudiantes})