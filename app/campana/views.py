import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from esterilizaya.constantes import PARROQUIAS_CANTON
from inscripcion.models import Inscripcion

from .forms import CampanaForm
from .models import Campana

logger = logging.getLogger(__name__)


@login_required(login_url="cuenta:login")
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


def mostrar(request, anio, parroquia, mes, dia):
    campana = get_object_or_404(Campana, creada__year=anio, parroquia=parroquia, creada__month=mes, creada__day=dia)
    n_registrados = Inscripcion.objects.filter(campana_id=campana.id).count()
    return render(request, "campana/campana.html", {"campana": campana, "n_registrados": n_registrados})


def listar_canton_parroquia(request):
    canton = request.GET.get("canton")
    if not canton:
        return JsonResponse({"parroquias": PARROQUIAS_CANTON})
    return JsonResponse({"parroquias": PARROQUIAS_CANTON.get(canton, [])})
