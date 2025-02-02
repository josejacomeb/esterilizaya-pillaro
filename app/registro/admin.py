from django.contrib import admin

from .models import Registro

# Register your models here.


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "numero_turno", "sexo", "especie", "foto", "obtener_campana_id"]
    list_filter = ("inscripcion__campana__id",)
    show_facets = admin.ShowFacets.ALWAYS

    @admin.display(description="Campaña ID")
    def obtener_campana_id(self, obj):
        return obj.inscripcion.campana.id if obj.inscripcion.campana else None
