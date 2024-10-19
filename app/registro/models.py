from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from esterilizaya.constantes import EDADES, ESPECIE, RAZON_TENENCIA, SEXO
from inscripcion.models import Inscripcion


class Registro(models.Model):
    class Meta:
        ordering = ["numero_turno"]

    inscripcion_id = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    # Encabezado
    peso = models.FloatField(
        help_text="Valor entre 0.1 y 100.0", validators=[MaxValueValidator(100.0), MinValueValidator(0.1)]
    )
    numero_turno = models.PositiveSmallIntegerField(
        help_text="Número turno", validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    # Datos generales
    nombre = models.CharField(max_length=40)
    color_principal = models.CharField(max_length=30, help_text="Color principal")
    color_secundario = models.CharField(max_length=30, help_text="Color secundario", blank=True)
    observaciones = models.CharField(max_length=200, blank=True)
    # Datos específicos
    especie = models.CharField(choices=ESPECIE, max_length=1)
    sexo = models.CharField(choices=SEXO, max_length=1)
    # TODO: Añadir edad en meses y días
    edad = models.CharField(choices=EDADES, max_length=2)
    raza_mascota = models.CharField(max_length=250)
    carnet = models.CharField(choices={"S": "Si", "N": "No"}, max_length=1, default="N")
    # Datos tutor
    nombres_tutor = models.CharField(max_length=250)
    numero_telefono_tutor = models.CharField(max_length=10)
    cedula_identidad = models.CharField(max_length=10)
    razon_tenencia = models.CharField(choices=RAZON_TENENCIA, max_length=2, default="CO")
    parroquia_tutor = models.CharField(max_length=250)
    barrio_tutor = models.CharField(max_length=250)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="registro")

    def __str__(self) -> str:
        return self.nombre
