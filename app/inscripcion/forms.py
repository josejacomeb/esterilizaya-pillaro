from django import forms
from .models import Inscripcion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombres_tutor', "barrio_tutor", "parroquia_tutor", "numero_telefono_tutor", "especie", "sexo", "horario"]
