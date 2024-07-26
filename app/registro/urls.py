from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="registro_index"),
    path("lista/<int:campana_id>", views.lista, name="registro_lista"),
    path("nuevo/<int:inscripcion_id>", views.registrar, name="registro_nuevo"),
    path("ficha/<int:registro_id>", views.ficha, name="registro_ficha"),
]
