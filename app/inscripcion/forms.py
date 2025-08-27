from django import forms

from .models import Inscripcion


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = [
            "nombres_tutor",
            "barrio_tutor",
            "parroquia_tutor",
            "numero_telefono_tutor",
            "horario",
            "cupos_totales",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["barrio_tutor"].widget.attrs.update(
            {
                "class": "form-control autocomplete",
                "autocomplete": "on",
                "data-suggestions-threshold": "1",
                "placeholder": "Escribe para buscar barrios registrados...",
            }
        )
