from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from esterilizaya.constantes import PARROQUIAS


class Campana(models.Model):
    """Modelo inicial sobre la campaña"""

    class Meta:
        ordering = ["fecha"]

    nombre = models.CharField(max_length=250)
    barrio = models.CharField(max_length=100)
    parroquia = models.CharField(choices=PARROQUIAS, max_length=100)
    fecha = models.DateField()
    n_animales = models.PositiveSmallIntegerField(
        help_text="Valor del 1 al 50", validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre
