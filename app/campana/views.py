import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CampanaForm
from .models import Campana

logger = logging.getLogger(__name__)


def index(request):
    if request.method == "POST":
        forma = CampanaForm(request.POST)
        if forma.is_valid():
            usuario = User.objects.get(username=request.user)
            instancia = forma.save(commit=False)
            instancia.usuario = usuario
            instancia.save()
            messages.success(request, "¡Campaña registrada exitosamente!")
            return redirect("inicio:index")
        else:
            forma.clean()
            messages.error(request, "Errores de validacion en los datos")
    else:
        forma = CampanaForm()
    return render(request, "campana/registro.html", {"form": forma})


def mostrar(request, year, parroquia, barrio):
    campana = get_object_or_404(Campana, creada__year=year, parroquia=parroquia, barrio=barrio)
    logger.info(campana)
    return render(request, "campana/campana.html", {"campana": campana})
