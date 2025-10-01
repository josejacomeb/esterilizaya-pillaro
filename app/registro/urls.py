from django.urls import path

from . import views

app_name = "registro"
urlpatterns = [
    path("", views.index, name="index"),
    path("lista/<int:campana_id>", views.lista, name="lista"),
    path("nuevo/<int:campana_id>/<int:inscripcion_id>", views.registrar, name="nuevo"),
    path("ver_ficha/<int:campana_id>/<int:registro_id>", views.ver_ficha, name="ver_ficha"),
    path("ver_certificados/<int:campana_id>", views.ver_certificados, name="ver_certificados"),
    path("ver_recetas/<int:campana_id>", views.ver_recetas, name="ver_recetas"),
    path("vista_veterinarios/<int:campana_id>", views.RegistradoListView.as_view(), name="vista_veterinarios"),
    path("registro/<int:registro_id>/generar_pdf/", views.generar_pdf, name="generar_pdf"),
    path("razas/", views.obtener_razas, name="razas"),
    path("barrios/", views.obtener_barrios, name="barrios"),
    path(
        "ver/<int:id>",
        views.ver_mascota,
        name="ver",
    ),
]
