from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CampanaForm


def index(request):
    if request.method == "POST":
        forma = CampanaForm(request.POST)
        if forma.is_valid():
            forma.save()
            messages.success(request, "¡Campaña registrada exitosamente!")
            return redirect("inicio")
        else:
            forma.clean()
            messages.error(request, "Errores de validacion en los datos")
    else:
        forma = CampanaForm()
    return render(request, "campana/registro.html", {"form": forma})
