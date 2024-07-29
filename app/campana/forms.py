from django import forms

from .models import Campana


class DateInput(forms.DateInput):
    input_type = "date"


class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ["nombre", "barrio", "parroquia", "fecha", "n_animales"]
        widgets = {"fecha": DateInput()}
