import uuid
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from esterilizaya.constantes import (
    AFIRMATIVO_NEGATIVO,
    COLORES,
    EDADES_ANOS,
    EDADES_MESES,
    ESPECIE,
    N_MASCOTAS,
    PARROQUIAS,
    RAZON_TENENCIA,
    SEXO,
)
from inscripcion.models import Inscripcion


def obtener_url_unico(instance, filename):
    current_date = datetime.now()
    year_folder = current_date.strftime("%y")
    month_folder = current_date.strftime("%m")
    day_folder = current_date.strftime("%d")

    # Crear la ruta en 'mascotas/%y/%m/%d/'
    extension = filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return Path("mascotas") / year_folder / month_folder / day_folder / unique_filename


class Registro(models.Model):
    class Meta:
        ordering = ["numero_turno"]
        indexes = [
            models.Index(fields=["-fecha_registro"]),
        ]

    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    # Encabezado
    peso = models.FloatField(
        help_text="Valor entre 0.1 y 100.0", validators=[MaxValueValidator(100.0), MinValueValidator(0.1)], default=12
    )
    numero_turno = models.PositiveSmallIntegerField(
        help_text="Número turno", validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    # Datos generales
    nombre = models.CharField(max_length=40, help_text="Nombre mascota")
    color_principal = models.CharField(max_length=30, help_text="Color principal", choices=COLORES)
    color_secundario = models.CharField(max_length=30, help_text="Color secundario", blank=True, choices=COLORES)
    observaciones = models.CharField(max_length=200, blank=True)
    # Datos específicos
    especie = models.CharField(choices=ESPECIE, max_length=1)
    sexo = models.CharField(choices=SEXO, max_length=2)
    foto = models.ImageField(upload_to=obtener_url_unico, blank=True)
    edad_anos = models.PositiveSmallIntegerField(choices=EDADES_ANOS, default=0)
    edad_meses = models.PositiveSmallIntegerField(choices=EDADES_MESES, default=6)
    raza_mascota = models.CharField(max_length=250)
    carnet = models.CharField(choices=AFIRMATIVO_NEGATIVO, max_length=1, default="N")
    vulnerable = models.BooleanField(default=False)
    # Datos tutor
    nombres_tutor = models.CharField(max_length=250)
    numero_telefono_tutor = models.PositiveIntegerField(
        # Entre 7 y 10 dígitos
        validators=[MinValueValidator(1000000), MaxValueValidator(9999999999)]
    )
    cedula_identidad = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
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
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre} de {self.nombres_tutor}"
