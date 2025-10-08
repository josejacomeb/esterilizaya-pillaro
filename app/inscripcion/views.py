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
    campana = Campana.objects.filter(id=campana_id).first()
    max_cupos = []
    n_cupos = []
    for inscripcion in inscripciones:
        if inscripcion.cupos_totales > 0:
            n_cupos.append(inscripcion.cupos_totales)
        else:
            n_cupos.append(0)
        max_cupos.append(list(range(1, inscripcion.cupos_totales + 1)))
    inscripciones_cupos = zip(n_cupos, inscripciones, max_cupos)

    pendientes = []
    registrados = []

    for n_cupos, inscripcion, cupos in inscripciones_cupos:
        if n_cupos > inscripcion.cupos_registrados:
            pendientes.append((n_cupos, inscripcion, cupos))
        else:
            registrados.append((n_cupos, inscripcion, cupos))
    breadcrumbs = [
        {"titulo": campana.nombre, "url": campana.get_absolute_url()},
        {"titulo": "Todas inscripciones", "url": None},
    ]
    return render(
        request,
        "inscripcion/todos.html",
        {"pendientes": pendientes, "registrados": registrados, "campana": campana, "breadcrumbs": breadcrumbs},
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
        forma = InscripcionForm(campana=campana)
    breadcrumbs = [
        {"titulo": campana.nombre, "url": campana.get_absolute_url()},
        {"titulo": "Inscripciones", "url": f"{campana.get_absolute_url()}inscripciones/"},
    ]
    return render(request, "inscripcion/nueva.html", {"form": forma, "campana": campana, "breadcrumbs": breadcrumbs})
