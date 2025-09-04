from django import forms
from esterilizaya.constantes import SelectInput

from .models import Inscripcion


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = [
            "nombres_tutor",
            "canton_tutor",
            "parroquia_tutor",
            "barrio_tutor",
            "numero_telefono_tutor",
            "horario",
            "cupos_totales",
        ]
        widgets = {"parroquia_tutor": SelectInput()}

    def __init__(self, *args, campana=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["barrio_tutor"].widget.attrs.update(
            {
                "class": "form-control autocomplete",
                "autocomplete": "on",
                "data-suggestions-threshold": "1",
                "placeholder": "Escribe para buscar barrios registrados...",
            }
        )
        if campana:
            self.fields["canton_tutor"].initial = campana.canton
            self.fields["parroquia_tutor"].initial = campana.parroquia
