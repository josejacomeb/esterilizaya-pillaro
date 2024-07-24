from django.db import models
from inscripcion.models import Inscripcion
from django.core.validators import MaxValueValidator, MinValueValidator
from esterilizaya.constantes import SEXO, ESPECIE, EDADES

class Registro(models.Model):
    inscripcion_id = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    # Encabezado
    peso = models.FloatField(
        help_text="Valor entre 0.1 y 100.0", 
        validators=[MaxValueValidator(100.0), MinValueValidator(0.1)]
    )
    # Datos generales
    nombre = models.CharField(max_length=40)
    color_principal = models.CharField(max_length=30, help_text="Color principal")
    color_secundario = models.CharField(max_length=30, help_text="Color secundario")
    observaciones = models.CharField(max_length=200, null=True)
    # Datos específicos
    especie = models.CharField(choices=ESPECIE, max_length=20)
    sexo = models.CharField(choices=SEXO, max_length=20)
    # TODO: Añadir edad en meses y días
    edad = models.CharField(choices=EDADES, max_length=20)
    raza_mascota = models.CharField(max_length=250)
    carnet = models.TextChoices("Carnet", "Si No")
    # Datos tutor
    nombres_tutor = models.CharField(max_length=250)
    numero_telefono_tutor = models.CharField(max_length=10)
    cedula_identidad = models.CharField(max_length=10, help_text="Cédula de identidad")
    razon_tenencia = models.TextChoices("Razón Tenencia", "Compañia Guardián Reproductiva Deporte Caza Servicio Mixta")
    domicilio = models.CharField(max_length=50)