from django.urls import path

from . import views

app_name = "registro"
urlpatterns = [
    path("", views.index, name="index"),
    path("lista/<int:campana_id>", views.lista, name="lista"),
    path("nuevo/<int:campana_id>/<int:inscripcion_id>", views.registrar, name="nuevo"),
    path("ficha/<int:campana_id>/<int:registro_id>", views.ficha, name="ficha"),
]
