from django.db import models
from aplicaciones.docente.models import Docente

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    creditos = models.IntegerField(null=False, blank=False)
    nivel = models.CharField(max_length=20, null=False, blank=False)
    horas_semanales = models.IntegerField(null=False, blank=False)
    jornada = models.CharField(max_length=20, null=False, blank=False)
    imagen = models.ImageField(upload_to='curso', null=True, blank=True)
    docente = models.ForeignKey('docente.Docente', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
