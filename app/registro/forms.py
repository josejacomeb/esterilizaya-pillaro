import logging

from django import forms

from .models import Registro

logger = logging.getLogger(__name__)


class RegistroForm(forms.ModelForm):
    peso = forms.FloatField(widget=forms.NumberInput(attrs={"step": "0.1", "min": "0"}))

    class Meta:
        model = Registro
        exclude = ["inscripcion", "usuario"]

    def __init__(self, *args, **kwargs):
        self.inscripcion_campana_id = kwargs.pop("inscripcion_campana_id", None)
        super().__init__(*args, **kwargs)
        self.fields["raza_mascota"].initial = "Mestizo"

    def clean_numero_turno(self):
        numero_turno = self.cleaned_data.get("numero_turno")
        if Registro.objects.filter(
            numero_turno=numero_turno, inscripcion__campana__id=self.inscripcion_campana_id
        ).exists():
            raise forms.ValidationError(
                f"El turno {numero_turno} ya ha sido asignado a otro tutor, agregue el turno correcto."
            )
        return numero_turno
