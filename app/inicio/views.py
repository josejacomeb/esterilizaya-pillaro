from campana.models import Campana
from django.shortcuts import render


def index(request):
    activas = Campana.activas.all()
    pasadas = Campana.pasadas.all().order_by("-fecha")

    return render(request, "inicio/inicio.html", {"activas": activas, "pasadas": pasadas})
