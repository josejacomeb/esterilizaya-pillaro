from django.shortcuts import render, redirect, get_object_or_404
from campana.models import Campana
from inscripcion.models import Inscripcion
from registro.models import Registro
import logging
from .forms import RegistroForm
logger = logging.getLogger(__name__)

def index(request):
    campanas = Campana.objects.all()

    return render(request, "registro/index.html", {
        "campanas": campanas
    })
    

def lista(request, campana_id):
    inscripciones = Inscripcion.objects.filter(campana_id=campana_id).filter(registrado=False)
    query = ""
    if 'query' in request.GET:
        query = request.GET['query']
    if query:
        inscripciones = inscripciones.filter(nombres_tutor__iregex=query)

    return render(request, "registro/lista.html", {
        "inscripciones": inscripciones,
        "campana_id": campana_id
    })

def registrar(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        forma = RegistroForm(request.POST)
        if forma.is_valid():
            registro_forma = forma.save(commit=False)
            registro_forma.inscripcion_id = inscripcion
            inscripcion.registrado = True
            inscripcion.save()
            registro_forma.save()
            registro_id = registro_forma.id
            logger.info(f"Forma guardada! con id {registro_id}")
            logger.info(registro_forma)
            logger.info(type(registro_forma))
            return redirect("registro_ficha", registro_id=registro_id)
        else:
            forma.clean()
    else:
        forma = RegistroForm(instance=inscripcion)
        logger.info(type(forma))
        forma_b = RegistroForm()
        logger.info(type(forma_b))


    return render(request, "registro/nuevo.html", {
        "form": forma
    })

def ficha(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    logger.info(registro, registro_id)
    return render(request, "registro/ficha.html", {
        "registro": registro
    })
