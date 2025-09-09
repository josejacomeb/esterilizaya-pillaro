import logging

from django.core.paginator import Paginator
from django.shortcuts import render
from registro.models import Registro

logger = logging.getLogger(__name__)


def index(request):
    lista_registros = Registro.objects.all().order_by("id")
    paginator = Paginator(lista_registros, 25)
    page_number = request.GET.get("page", 1)
    registros = paginator.page(page_number)
    logger.info(registros)
    return render(request, "index.html", {"registros": registros})
