from django import forms
from .models import *

class Cliente(forms.ModelForm):

    class Meta:
        model = Clienteindividual
        fields = ("cui", "nit", "nombrecompleto", "fechanacimiento", "usuario", "contrasenia")
