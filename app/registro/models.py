from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from esterilizaya.constantes import (
    AFIRMATIVO_NEGATIVO,
    EDADES_ANOS,
    EDADES_MESES,
    ESPECIE,
    PARROQUIAS,
    RAZON_TENENCIA,
    SEXO,
    N_MASCOTAS,
)
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
    sexo = models.CharField(choices=SEXO, max_length=2)
    edad_anos = models.PositiveSmallIntegerField(choices=EDADES_ANOS, default=0)
    edad_meses = models.PositiveSmallIntegerField(choices=EDADES_MESES, default=6)
    raza_mascota = models.CharField(max_length=250)
    carnet = models.CharField(choices=AFIRMATIVO_NEGATIVO, max_length=1, default="N")
    # Datos tutor
    nombres_tutor = models.CharField(max_length=250)
    numero_telefono_tutor = models.CharField(max_length=10)
    cedula_identidad = models.CharField(max_length=10)
    razon_tenencia = models.CharField(choices=RAZON_TENENCIA, max_length=2, default="CO")
    parroquia_tutor = models.CharField(choices=PARROQUIAS, max_length=100)
    barrio_tutor = models.CharField(max_length=250)
    # Porcentaje esterilización
    n_animales_hogar = models.SmallIntegerField(
        choices=N_MASCOTAS, default="3", help_text="Total perros y gatos en el hogar"
    )
    n_animales_hogar_esterilizadas = models.SmallIntegerField(
        choices=N_MASCOTAS, default="0", help_text="Total perros y gatos esterilizados en el hogar"
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="registro")

    def __str__(self) -> str:
        return self.nombre
