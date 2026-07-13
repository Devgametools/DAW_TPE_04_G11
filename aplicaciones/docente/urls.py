from django.urls import path

from .views import crearDocente, docentes, editarDocente, eliminarDocente

app_name = 'docentes'

urlpatterns = [
    path('docentes/', docentes.as_view(), name='listar'),
    path('docentes/registrar/', crearDocente.as_view(), name='crear'),
    path('docentes/editar/<int:pk>/', editarDocente.as_view(), name='editar_docente'),
    path('docentes/eliminar/<int:pk>/', eliminarDocente.as_view(), name='eliminar_docente')
]