from django.contrib import admin

from .models import Registro

# Register your models here.


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "numero_turno", "nombres_tutor", "sexo", "especie", "obtener_campana_id", "barrio_tutor"]
    list_filter = ("inscripcion__campana__id", "barrio_tutor")
    show_facets = admin.ShowFacets.ALWAYS

    @admin.display(description="Campaña ID")
    def obtener_campana_id(self, obj):
        return obj.inscripcion.campana.id if obj.inscripcion.campana else None
