from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from aplicaciones.docente.models import Docente

# Create your models here.
class Curso(models.Model):
    NIVEL_CHOICES = [
        (1, 'Nivel 1'),
        (2, 'Nivel 2'),
        (3, 'Nivel 3'),
        (4, 'Nivel 4'),
        (5, 'Nivel 5'),
        (6, 'Nivel 6'),
        (7, 'Nivel 7'),
        (8, 'Nivel 8'),
        (9, 'Nivel 9'),
        (10, 'Nivel 10'),
    ]

    JORNADA_CHOICES = [
        ('MATUTINA', 'Matutina'),
        ('VESPERTINA', 'Vespertina'),
        ('NOCTURNA', 'Nocturna'),
    ]

    nombre = models.CharField(max_length=100, null=False, blank=False)
    creditos = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    nivel = models.PositiveSmallIntegerField(
        choices=NIVEL_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Nivel de la malla curricular (1 a 10).',
    )
    horas_semanales = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(40)]
    )
    jornada = models.CharField(max_length=20, null=False, blank=False, choices=JORNADA_CHOICES)
    imagen = models.ImageField(upload_to='curso', null=True, blank=True)
    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        related_name='cursos',
        verbose_name='Docente'
    )
    def __str__(self):
        return self.nombre
