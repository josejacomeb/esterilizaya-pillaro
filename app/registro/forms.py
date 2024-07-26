from django import forms
from .models import Registro
import logging
logger = logging.getLogger(__name__)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        #fields = "__all__"
        exclude = ["inscripcion_id"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raza_mascota'].initial = 'Mestizo'