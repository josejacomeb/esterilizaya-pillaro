import logging

from campana.models import Campana
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from inscripcion.models import Inscripcion
from registro.models import Registro
from django.http import JsonResponse

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
    # CChequear si hay cupos disponibles
    if inscripcion.cupos_registrados >= inscripcion.cupos_totales:
        return JsonResponse({
            "success": False,
            "message": f"No hay más cupos para registrar este tutor {inscripcion.nombres_tutor}"
        }, status=400)
    
    if request.method == "POST":
        forma = RegistroForm(request.POST)
        if forma.is_valid():
            registro_forma = forma.save(commit=False)
            usuario = User.objects.get(username=request.user)
            registro_forma.inscripcion = inscripcion
            registro_forma.usuario = usuario
            inscripcion.cupos_registrados += 1
            inscripcion.save()
            registro_forma.save()
            registro_id = registro_forma.id
            return redirect("registro:ficha", campana_id=campana_id, registro_id=registro_id)
        else:
            forma.clean()
    else:
        forma = RegistroForm(instance=inscripcion)

    return render(request, "registro/nuevo.html", {"form": forma})


def ficha(request, campana_id, registro_id):
    registro = get_object_or_404(Registro, id=registro_id, inscripcion__campana=campana_id)
    return render(request, "registro/ficha.html", {"registro": registro})
