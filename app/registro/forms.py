import logging

from django import forms

from .models import Registro

logger = logging.getLogger(__name__)


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        exclude = ["inscripcion_id", "usuario"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["raza_mascota"].initial = "Mestizo"
