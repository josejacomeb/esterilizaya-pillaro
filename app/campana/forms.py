from django import forms
from esterilizaya.constantes import SelectInput

from .models import Campana


class DateInput(forms.DateInput):
    input_type = "date"


class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ["nombre", "canton", "parroquia", "barrio", "fecha", "n_animales"]
        widgets = {"fecha": DateInput(), "parroquia": SelectInput()}
