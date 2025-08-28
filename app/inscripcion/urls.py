from django.urls import path

from . import views

app_name = "inscripcion"
urlpatterns = [
    path("<int:campana_id>/", views.index, name="index"),
    path("crear/<int:campana_id>/", views.crear, name="create"),
    path("barrios/", views.obtener_barrios, name="barrios"),
]
