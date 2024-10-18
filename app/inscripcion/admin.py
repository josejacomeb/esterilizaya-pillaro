from django.contrib import admin

from .models import Inscripcion


# Register your models here.
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = [
        "nombres_tutor",
        "barrio_tutor",
        "parroquia_tutor",
        "registrado",
        "numero_telefono_tutor",
        "especie",
        "sexo",
        "horario",
        "campana",
    ]
    search_fields = ["nombres_tutor", "campana"]
    show_facets = admin.ShowFacets.ALWAYS
