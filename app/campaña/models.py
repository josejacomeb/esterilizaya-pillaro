from django.db import models
import datetime

class Campaña(models.Model):
    """Modelo inicial sobre la campaña"""
    nombre = models.CharField(max_length=250)
    colaboradores = models.TextField()
    fecha = models.DateField(initial=datetime.date.today)
    animales = models.Choices(list(range(0, 50)))