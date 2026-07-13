from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Docente(models.Model):
    TIPOS_SANGRE = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    validador_cedula = RegexValidator(
        regex=r'^\d{10}$',
        message='La cedula debe contener exactamente 10 digitos numericos.'
    )

    cedula = models.CharField(max_length=10, unique=True, null=False, blank=False, validators=[validador_cedula], help_text='Numero de cedula (10 digitos).')
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField()
    tipo_sangre = models.CharField(max_length=5, null=True, blank=True, choices=TIPOS_SANGRE)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='docente', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
