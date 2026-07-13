from django.urls import path

from .views import crearCurso, editarCurso, verCursos, eliminarCurso

app_name = 'materias'

urlpatterns = [
    path('cursos/', verCursos.as_view(), name='listar'),
    path('cursos/registrarCurso/', crearCurso.as_view(), name='crear'),
    path('cursos/editarCurso/<int:pk>/', editarCurso.as_view(), name='editar_curso'),
    path('cursos/eliminarCurso/<int:pk>/', eliminarCurso.as_view(), name='eliminar_curso')
]