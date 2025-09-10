from django.urls import path

from . import views

app_name = "mascotas"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "ver/<int:campana_id>/<str:canton_tutor>/<str:parroquia_tutor>/<str:barrio_tutor>/<int:id>",
        views.ver_mascota,
        name="ver",
    ),
]
