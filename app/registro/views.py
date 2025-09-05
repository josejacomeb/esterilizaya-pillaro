import logging

from campana.models import Campana
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic import ListView
from esterilizaya.constantes import RUTA_PDFS
from inscripcion.models import Inscripcion
from registro.models import Registro
from weasyprint import HTML

from .forms import RegistroForm

logger = logging.getLogger(__name__)


def index(request):
    campanas = Campana.objects.all()

    return render(request, "registro/index.html", {"campanas": campanas})


def lista(request, campana_id):
    registros = Registro.objects.filter(inscripcion__campana=campana_id)
    # Dato del primer resultado
    nombre_campana = registros[0].inscripcion.campana.nombre
    query = ""
    if "query" in request.GET:
        query = request.GET["query"]
    if query:
        registros = registros.filter(nombres_tutor__iregex=query)
    return render(
        request,
        "registro/lista.html",
        {"registros": registros, "campana_id": campana_id, "nombre_campana": nombre_campana},
    )


@login_required(login_url="cuenta:login")
def registrar(request, campana_id, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id, campana_id=campana_id)
    # Chequear si hay cupos disponibles
    if inscripcion.cupos_registrados >= inscripcion.cupos_totales:
        messages.error(request, f"Lo siento, ya no hay más cupos disponibles para {inscripcion.nombres_tutor}")
        return redirect("inscripcion:index", campana_id=inscripcion.campana.id)
    if request.method == "POST":
        forma = RegistroForm(request.POST, request.FILES, inscripcion_campana_id=campana_id)
        if forma.is_valid():
            registro_forma = forma.save(commit=False)
            usuario = User.objects.get(username=request.user)
            registro_forma.inscripcion = inscripcion
            registro_forma.usuario = usuario
            inscripcion.cupos_registrados += 1
            inscripcion.save()
            registro_forma.save()
            registro_id = registro_forma.id
            return redirect("registro:ver_ficha", campana_id=campana_id, registro_id=registro_id)
        else:
            forma.clean()
    else:
        registro_anterior = (
            Registro.objects.filter(
                inscripcion__campana_id=campana_id, inscripcion__nombres_tutor=inscripcion.nombres_tutor
            )
            .order_by("-id")
            .first()
        )
        initial_data = {}
        if registro_anterior:
            logger.info(registro_anterior)
            initial_data = {
                "cedula_identidad": registro_anterior.cedula_identidad,
                "n_animales_hogar": registro_anterior.n_animales_hogar,
                "n_animales_hogar_esterilizadas": registro_anterior.n_animales_hogar_esterilizadas,
            }
        forma = RegistroForm(instance=inscripcion, inscripcion_campana_id=campana_id, initial=initial_data)
    return render(request, "registro/nuevo.html", {"form": forma})


def ver_ficha(request, campana_id, registro_id):
    registro = get_object_or_404(Registro, id=registro_id, inscripcion__campana=campana_id)
    return render(request, "registro/ficha.html", {"registro": registro})


def imprimir_ficha(request, campana_id, registro_id):
    registro = get_object_or_404(Registro, id=registro_id, inscripcion__campana=campana_id)
    return render(request, "registro/ficha.html", {"registro": registro})


# TODO: Simplificar todos los registros
def ver_certificados(request, campana_id):
    registros = Registro.objects.filter(inscripcion__campana=campana_id)
    return render(request, "registro/hoja_certificados.html", {"registros": registros})


def ver_recetas(request, campana_id):
    registros = Registro.objects.filter(inscripcion__campana=campana_id)
    return render(request, "registro/recetas/hoja_recetas.html", {"registros": registros})


class RegistradoListView(ListView):
    model = Registro
    template_name = "registro/vista_veterinarios.html"
    context_object_name = "registros"

    def get_queryset(self):
        """
        Filters pets by the given campaign_id.
        """
        campana_id = self.kwargs.get("campana_id")  # Retrieve campaign_id from URL kwargs
        return Registro.objects.filter(inscripcion__campana=campana_id)  # Filter pets for the given campaign

    def get(self, request, *args, **kwargs):
        """
        Handles AJAX requests to dynamically update the table.
        """
        campana_id = self.kwargs.get("campana_id")
        if request.headers.get("x-requested-with") == "XMLHttpRequest":  # Check for Ajax requests
            registros = list(
                Registro.objects.filter(inscripcion__campana=campana_id).values(
                    "foto",
                    "especie",
                    "peso",
                    "nombre",
                    "vulnerable",
                    "sexo",
                    "edad_anos",
                    "edad_meses",
                    "fecha_registro",
                    "observaciones",
                    "numero_turno",
                    "nombres_tutor",
                )
            )

            return JsonResponse({"registros": registros})
        return super().get(request, *args, **kwargs)


def generar_pdf(request, registro_id):
    # TODO: Eliminar esto cuando el SSL sea global
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    registro = get_object_or_404(Registro, id=registro_id)
    html_string = render_to_string("registro/ficha.html", {"registro": registro, "pdf_mode": True})
    if not RUTA_PDFS.exists():
        RUTA_PDFS.mkdir(parents=True, exist_ok=True)
    ruta_ficha_pdf = RUTA_PDFS / f"ficha_{registro.numero_turno}_{registro.nombre}_{registro_id}.pdf"
    try:
        HTML(
            string=html_string,
            base_url=request.build_absolute_uri(),
        ).write_pdf(ruta_ficha_pdf)
        logging.info(f"PDF guardado en: {ruta_ficha_pdf}")
        messages.success(request, "PDF generado y guardado exitosamente.")
    except Exception as e:
        logging.error(f"Error al guardar el PDF: {e}")
        messages.error(request, "Error al generar el PDF. Por favor, inténtelo de nuevo más tarde.")
        return redirect("registro:ver_ficha", campana_id=registro.inscripcion.campana.id, registro_id=registro_id)
    return redirect("registro:lista", campana_id=registro.inscripcion.campana.id)


def obtener_razas(request):
    query = request.GET.get("term", "")
    # Obtener razas únicas de registros en campañas pasadas y que sus nombres hayan sido corregidos
    # para que coincidan con la consulta via AJAX
    raza_mascota = (
        Registro.objects.filter(raza_mascota__icontains=query, inscripcion__campana__estado=Campana.Estado.PASADA)
        .order_by("raza_mascota")
        .values_list("raza_mascota", flat=True)
        .distinct()
    )
    return JsonResponse(list(raza_mascota), safe=False)


def obtener_barrios(request):
    query = request.GET.get("term", "")
    barrio_tutor = (
        Registro.objects.filter(barrio_tutor__icontains=query, inscripcion__campana__estado=Campana.Estado.PASADA)
        .order_by("barrio_tutor")
        .values_list("barrio_tutor", flat=True)
        .distinct()
    )
    return JsonResponse(list(barrio_tutor), safe=False)
