from campana.models import Campana
from django.shortcuts import render


def index(request):
    activas = Campana.activas.all()
    pasadas = Campana.pasadas.all()
    print(request.user)

    return render(request, "inicio/inicio.html", {"activas": activas, "pasadas": pasadas, "user": request.user})
