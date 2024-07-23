from django.shortcuts import render, redirect
from .models import Inscripcion
from campana.models import Campana
from .forms import InscripcionForm
import logging

logger = logging.getLogger(__name__)
def index(request):
    inscripciones = Inscripcion.objects.all()
    logger.info(inscripciones)
    return render(request, "inscripcion/todos.html", {
        "inscripciones": inscripciones
    })

def crear(request):
    # TODO: Mandar a crear una nueva campaña sino existe
    if request.method == 'POST':
        forma = InscripcionForm(request.POST)
        if forma.is_valid():
            campana_id = request.POST.get('campana_id')
            nueva_inscripcion = forma.save(commit = False)
            logger.info(campana_id)

            nueva_inscripcion.campana_id = campana_id
            nueva_inscripcion.save()
            return redirect("inscripcion_index")
        else:
            forma.clean()
    else:
        forma = InscripcionForm()
    campanas = Campana.objects.all()
    return render(request, "inscripcion/nueva.html", {
        "form": forma,
        "campanas": campanas
    })
