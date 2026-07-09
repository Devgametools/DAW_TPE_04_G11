from django.db import models

# Create your models here.
class Docente(models.Model):
    cedula = models.CharField(max_length=10, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField()
    tipo_sangre = models.CharField(max_length=5, null=True, blank=True)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='docente', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
