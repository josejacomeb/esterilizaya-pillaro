from campana.models import Campana
from django.db import models
from esterilizaya.constantes import ESPECIE, HORARIOS, PARROQUIAS, SEXO


class Inscripcion(models.Model):
    class Meta:
        ordering = ["nombres_tutor"]

    nombres_tutor = models.CharField(max_length=250)
    barrio_tutor = models.CharField(max_length=250)
    parroquia_tutor = models.CharField(choices=PARROQUIAS, max_length=100)
    numero_telefono_tutor = models.CharField(max_length=10)
    especie = models.CharField(choices=ESPECIE, max_length=20)
    sexo = models.CharField(choices=SEXO, max_length=20)
    horario = models.CharField(choices=HORARIOS, max_length=20)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    registrado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.especie + self.nombres_tutor
