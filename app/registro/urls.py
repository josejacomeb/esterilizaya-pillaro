from django.urls import path

from . import views

app_name = "registro"
urlpatterns = [
    path("", views.index, name="index"),
    path("lista/<int:campana_id>", views.lista, name="lista"),
    path("nuevo/<int:campana_id>/<int:inscripcion_id>", views.registrar, name="nuevo"),
    path("ver_ficha/<int:campana_id>/<int:registro_id>", views.ver_ficha, name="ver_ficha"),
    path("imprimir_ficha/<int:campana_id>/<int:registro_id>", views.imprimir_ficha, name="imprimir_ficha"),
    path("ver_certificados/<int:campana_id>", views.ver_certificados, name="ver_certificados"),
    path("ver_recetas/<int:campana_id>", views.ver_recetas, name="ver_recetas"),
    path("vista_veterinarios/<int:campana_id>", views.RegistradoListView.as_view(), name="vista_veterinarios"),
]
