import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from registro.models import Registro

logger = logging.getLogger(__name__)


def index(request):
    lista_registros = Registro.objects.all().order_by("id")
    paginator = Paginator(lista_registros, 25)
    page_number = request.GET.get("page", 1)
    registros = paginator.page(page_number)
    return render(request, "index.html", {"registros": registros})

def ver_mascota(request, campana_id, canton_tutor, parroquia_tutor, barrio_tutor, id):
    registro = get_object_or_404(Registro, id=id)
    return render(request, "mascota.html", {"registro": registro})
    