import logging

from campana.models import Campana
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import InscripcionForm
from .models import Inscripcion

logger = logging.getLogger(__name__)


@login_required(login_url="cuenta:login")
def index(request, campana_id):
    inscripciones = Inscripcion.objects.filter(campana_id=campana_id)
    campana = inscripciones[0].campana
    max_cupos = [list(range(1, inscripcion.cupos_totales + 1)) for inscripcion in inscripciones]
    total_inscritos = 0
    for inscripcion in inscripciones:
        total_inscritos += inscripcion.cupos_totales
    inscripciones_cupos = zip(inscripciones, max_cupos)
    return render(
        request,
        "inscripcion/todos.html",
        {"inscripciones_cupos": inscripciones_cupos, "campana": campana, "total_inscritos": total_inscritos},
    )


@login_required(login_url="cuenta:login")
def crear(request, campana_id):
    campana = get_object_or_404(Campana, id=campana_id, estado=Campana.Estado.ACTIVA)
    if request.method == "POST":
        forma = InscripcionForm(request.POST)
        if forma.is_valid():
            usuario = User.objects.get(username=request.user)
            nueva_inscripcion = forma.save(commit=False)

            nueva_inscripcion.campana = campana
            nueva_inscripcion.usuario = usuario

            nueva_inscripcion.save()
            return redirect("inscripcion:index", campana_id)
        else:
            forma.clean()
    else:
        forma = InscripcionForm()
    campanas = Campana.objects.all()
    return render(request, "inscripcion/nueva.html", {"form": forma, "campanas": campanas})
