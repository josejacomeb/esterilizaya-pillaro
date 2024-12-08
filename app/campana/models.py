import logging

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from esterilizaya.constantes import PARROQUIAS

logger = logging.getLogger(__name__)


class ActivasManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado=Campana.Estado.ACTIVA)


class PasadasManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado=Campana.Estado.PASADA)


class Campana(models.Model):
    """Modelo inicial sobre la campaña"""

    class Estado(models.TextChoices):
        ACTIVA = "AC", "Activa"
        PASADA = "PA", "Pasada"

    class Meta:
        ordering = ["fecha"]

    nombre = models.CharField(max_length=250)
    barrio = models.CharField(max_length=100)
    parroquia = models.CharField(choices=PARROQUIAS, max_length=3, unique_for_date="creada")
    fecha = models.DateField()
    n_animales = models.PositiveSmallIntegerField(
        help_text="Valor del 1 al 50", validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=2, choices=Estado, default=Estado.ACTIVA)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="campana")
    objects = models.Manager()
    activas = ActivasManager()
    pasadas = PasadasManager()

    def __str__(self) -> str:
        return self.nombre

    def get_absolute_url(self):
        return reverse("campana:mostrar", args=[self.creada.year, self.parroquia, self.creada.month, self.creada.day])
