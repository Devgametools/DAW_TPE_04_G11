from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
class crearDocente(CreateView):
  template_name = "registrarDocente.html"
  model = Docente
  fields = "__all__"
  success_url = "/docentes"

class docentes(ListView):
  template_name = "docentes.html"
  model = Docente
  context_object_name = "docentes"

class editarDocente(UpdateView):
  template_name = "editarDocente.html"
  model = Docente
  fields = "__all__"
  success_url = "/docentes"

class eliminarDocente(DeleteView):
  template_name = "eliminarDocente.html"
  model = Docente
  context_object_name = "docente"
  success_url = "/docentes"
