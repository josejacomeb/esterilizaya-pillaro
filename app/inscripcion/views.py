import logging

from campana.models import Campana
from django.shortcuts import redirect, render

from .forms import InscripcionForm
from .models import Inscripcion

logger = logging.getLogger(__name__)


def index(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "inscripcion/todos.html", {"inscripciones": inscripciones})


def crear(request):
    # TODO: Mandar a crear una nueva campaña sino existe
    if request.method == "POST":
        forma = InscripcionForm(request.POST)
        if forma.is_valid():
            campana_id = request.POST.get("campana_id")
            nueva_inscripcion = forma.save(commit=False)

            nueva_inscripcion.campana_id = campana_id
            nueva_inscripcion.save()
            return redirect("inscripcion:index")
        else:
            forma.clean()
    else:
        forma = InscripcionForm()
    campanas = Campana.objects.all()
    return render(request, "inscripcion/nueva.html", {"form": forma, "campanas": campanas})
