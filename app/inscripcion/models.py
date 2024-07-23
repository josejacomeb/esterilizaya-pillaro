from django.db import models

ESPECIE = ["Canino", "Felino"]
SEXO = ["Macho", "Hembra"]

# Create your models here.
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


