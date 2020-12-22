from django import forms
from .models import *

class Cliente(forms.ModelForm):

    class Meta:
        model = Clienteindividual
        fields = ("cui", "nit", "nombrecompleto", "fechanacimiento", "usuario", "contrasenia")

class Empresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ("idtipoempresa", "nombre", "nombrecomercial", "nombrerepresentantelegal", "usuario", "contrasenia")