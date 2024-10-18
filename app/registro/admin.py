from django.contrib import admin

from .models import Registro

# Register your models here.


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ["nombre", "numero_turno", "sexo", "especie"]
    show_facets = admin.ShowFacets.ALWAYS
