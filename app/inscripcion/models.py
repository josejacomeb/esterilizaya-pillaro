from campana.models import Campana
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from esterilizaya.constantes import (
    CANTONES,
    HORARIOS,
    MAX_CUPOS,
    MAX_LONG_BARRIOS,
    MAX_LONG_CANTONES,
    MAX_LONG_PARROQUIAS,
    PARROQUIAS,
)


class Inscripcion(models.Model):
    class Meta:
        ordering = ["nombres_tutor"]

    nombres_tutor = models.CharField(max_length=250, help_text="Al menos un nombre y apellido del tutor")
    canton_tutor = models.CharField(
        choices=CANTONES, max_length=MAX_LONG_CANTONES, default="PI", help_text="Cantón residencia mascota"
    )
    parroquia_tutor = models.CharField(
        choices=PARROQUIAS, max_length=MAX_LONG_PARROQUIAS, help_text="Parroquia residencia mascota"
    )
    barrio_tutor = models.CharField(max_length=MAX_LONG_BARRIOS, help_text="Barrio residencia mascota")
    numero_telefono_tutor = models.PositiveIntegerField(
        # Entre 7 y 10 dígitos
        validators=[MinValueValidator(1000000), MaxValueValidator(9999999999)],
        help_text="Teléfono celular o convencional, en caso de no haber escribe 0900000000",
    )
    horario = models.CharField(choices=HORARIOS, max_length=2, help_text="Horario deseado del tutor")
    cupos_totales = models.SmallIntegerField(choices=MAX_CUPOS, default="1", help_text="Máximo cupos tutor por jornada")
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    cupos_registrados = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inscripcion")

    def __str__(self) -> str:
        return self.nombres_tutor + self.horario
