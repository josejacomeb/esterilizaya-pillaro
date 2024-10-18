from django.contrib import admin

from .models import Campana


# Register your models here.
@admin.register(Campana)
class CampanaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha", "barrio", "parroquia"]
    list_filter = ["barrio", "parroquia"]
    ordering = ["fecha"]
    show_facets = admin.ShowFacets.ALWAYS
