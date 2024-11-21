from campana.models import Campana
from django.conf import settings
from django.db import models
from esterilizaya.constantes import ESPECIE, HORARIOS, PARROQUIAS, SEXO, MAX_CUPOS
from django.core.validators import MaxValueValidator, MinValueValidator


class Inscripcion(models.Model):
    class Meta:
        ordering = ["nombres_tutor"]

    nombres_tutor = models.CharField(max_length=250)
    barrio_tutor = models.CharField(max_length=250)
    parroquia_tutor = models.CharField(choices=PARROQUIAS, max_length=100)
    numero_telefono_tutor = models.PositiveIntegerField(
        # Entre 7 y 10 dígitos
        validators=[MinValueValidator(1000000), MaxValueValidator(9999999999)]
    )
    horario = models.CharField(choices=HORARIOS, max_length=2)
    cupos_totales = models.SmallIntegerField(choices=MAX_CUPOS, default="1")
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    cupos_registrados = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inscripcion")

    def __str__(self) -> str:
        return self.nombres_tutor + self.horario
