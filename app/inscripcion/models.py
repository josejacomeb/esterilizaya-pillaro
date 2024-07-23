from django.db import models
from campana.models import Campana
ESPECIE = {
    "C": "Canino", 
    "F": "Felino"
}
SEXO = {
    "M": "Macho",
    "H": "Hembra"
}

PARROQUIAS = {
    # Rurales
    "BM": "Baquerizo Moreno",
    "EMT": "Emilio Maria Terán",
    "ME": "Marcos Espinel",
    "PU": "Presidente Urbina",
    "SA": "San Andrés",
    "SM": "San Miguelito",
    # Urbanas
    "LM": "La Matriz", 
    "CN": "Ciudad Nueva",
}

class Inscripcion(models.Model):
    nombres_tutor = models.CharField(max_length=250)
    raza_mascota = models.CharField(max_length=250)
    barrio_tutor = models.CharField(max_length=250)
    parroquia_tutor = models.CharField(choices=PARROQUIAS, max_length=100)
    numero_telefono_tutor = models.CharField(max_length=10)
    especie = models.CharField(choices=ESPECIE, max_length=20)
    sexo = models.CharField(choices=SEXO, max_length=20)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)



