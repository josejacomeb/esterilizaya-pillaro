import logging

from campana.models import Campana
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from inscripcion.models import Inscripcion
from registro.models import Registro

from .forms import RegistroForm

logger = logging.getLogger(__name__)


def index(request):
    campanas = Campana.objects.all()

    return render(request, "registro/index.html", {"campanas": campanas})


def lista(request, campana_id):
    registros = Registro.objects.filter(inscripcion__campana=campana_id)
    query = ""
    if "query" in request.GET:
        query = request.GET["query"]
    if query:
        registros = registros.filter(nombres_tutor__iregex=query)
    logger.info(registros)

    return render(request, "registro/lista.html", {"registros": registros, "campana_id": campana_id})


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
        forma = RegistroForm(instance=inscripcion, inscripcion_campana_id=campana_id)

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
