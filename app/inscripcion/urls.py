from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="inscripcion_index"),
    path("crear", views.crear, name="inscripcion_create"),
    path("ver/<int:inscr_id>", views.index, name="inscripcion_show"),
    path("guardar", views.index, name="inscripcion_store"),
    path("editar/<int:inscr_id>", views.index, name="inscripcion_edit"),
    # TODO: Borrar, modificar
]
