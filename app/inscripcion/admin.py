from django.contrib import admin

from .models import Inscripcion


# Register your models here.
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = [
        "nombres_tutor",
        "barrio_tutor",
        "parroquia_tutor",
        "cupos_totales",
        "cupos_registrados",
        "numero_telefono_tutor",
        "horario",
        "campana",
    ]
    search_fields = ["nombres_tutor", "campana"]
    show_facets = admin.ShowFacets.ALWAYS
