import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from esterilizaya.constantes import PARROQUIAS_CANTON
from inscripcion.models import Inscripcion
from registro.models import Registro

from .forms import CampanaForm
from .models import Campana

logger = logging.getLogger(__name__)


def campanas_activas(request):
    return {"campanas_activas": Campana.activas.all()}


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
    campana = get_object_or_404(Campana, fecha__year=anio, parroquia=parroquia, fecha__month=mes, fecha__day=dia)
    n_inscritos = Inscripcion.objects.filter(campana_id=campana.id).aggregate(total=Sum("cupos_totales"))
    n_registrados = Registro.objects.filter(inscripcion__campana_id=campana.id).count()
    breadcrumbs = [
        {"titulo": campana.nombre, "url": campana.get_absolute_url()},
    ]
    return render(
        request,
        "campana/campana.html",
        {
            "campana": campana,
            "n_registrados": n_registrados,
            "n_inscritos": n_inscritos["total"],
            "breadcrumbs": breadcrumbs,
        },
    )


def listar_canton_parroquia(request):
    canton = request.GET.get("canton")
    if not canton:
        return JsonResponse({"parroquias": PARROQUIAS_CANTON})
    return JsonResponse({"parroquias": PARROQUIAS_CANTON.get(canton, [])})
