import logging

from django import forms

from .models import Registro

logger = logging.getLogger(__name__)


class RegistroForm(forms.ModelForm):
    peso = forms.FloatField(widget=forms.NumberInput(attrs={"step": "0.1", "min": "0"}))

    class Meta:
        model = Registro
        exclude = ["inscripcion_id", "usuario"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["raza_mascota"].initial = "Mestizo"
