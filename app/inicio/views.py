from datetime import datetime

from campana.models import Campana
from django.db.models import Count
from django.shortcuts import render
from registro.models import Registro


def ver_campanas(request):
    activas = Campana.activas.all()
    pasadas = Campana.pasadas.all().order_by("-fecha")

    return render(request, "inicio/todas_campanas.html", {"activas": activas, "pasadas": pasadas})


def index(request):
    ahora = datetime.now()
    registros = Registro.objects.all()
    total = {
        "mascotas": registros.count(),
        "cantones": registros.values("canton_tutor").distinct().count(),
        "parroquias": registros.values("parroquia_tutor").distinct().count(),
        "barrios": registros.values("barrio_tutor").distinct().count(),
    }

    campana_hoy = Campana.objects.filter(fecha__year=ahora.year, fecha__month=ahora.month, fecha__day=ahora.day).first()

    hoy = {}
    if campana_hoy:
        registros_hoy = registros.filter(inscripcion__campana=campana_hoy.id)
        hoy["mascotas"] = registros_hoy.count()
        total_sexo = registros_hoy.values("sexo").annotate(total=Count("sexo"))
        hoy["machos"] = next((s["total"] for s in total_sexo if s["sexo"] == "♂️"), 0)
        hoy["hembras"] = next((s["total"] for s in total_sexo if s["sexo"] == "♀️"), 0)
        hoy["tutores"] = registros_hoy.values("nombres_tutor").distinct().count()

    return render(
        request,
        "inicio/index.html",
        {
            "total": total,
            "hoy": hoy,
        },
    )
