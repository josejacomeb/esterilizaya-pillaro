from django.urls import path

from . import views

app_name = "inscripcion"
urlpatterns = [
    path("", views.index, name="index"),
    path("crear", views.crear, name="create"),
    path("ver/<int:inscr_id>", views.index, name="show"),
    path("guardar", views.index, name="store"),
    path("editar/<int:inscr_id>", views.index, name="edit"),
    # TODO: Borrar, modificar
]
