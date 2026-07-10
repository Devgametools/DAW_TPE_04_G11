from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import *

# Create your views here.
class crearCurso(CreateView):
  template_name = "registrarcurso.html"
  model = Curso
  fields = "__all__"
  success_url = "/cursos"

class verCursos(ListView):
  template_name = "cursos.html"
  model = Curso
  context_object_name = "cursos"
