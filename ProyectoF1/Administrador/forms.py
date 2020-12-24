from django import forms
from .models import *

class Cliente(forms.ModelForm):
    class Meta:
        model = Clienteindividual
        fields = ("cui", "nit", "nombrecompleto", "fechanacimiento", "usuario", "contrasenia")


class Empresaa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ("idtipoempresa", "nombre", "nombrecomercial", "nombrerepresentantelegal", "usuario", "contrasenia")


class CuentaMonetaria(forms.Form):
    codigocuenta = forms.IntegerField(required=True, label="Codigo de la cuenta")
    montopormanejo = forms.DecimalField(required=True, label="Monto por manejo")
    saldo = forms.DecimalField(required=True, label="Saldo")
    lstipoCliente = [(1,"Cliente individual"), (2, "Empresa")]
    tipocliente = forms.CharField(widget=forms.Select(choices=lstipoCliente))
    idcliente = forms.IntegerField(required=True, label="Cui del cliente o ID de la Empresa")

    class Meta:
        model = Cuentamonetaria
        fields = ('codigocuenta', 'montopormanejo', 'saldo', 'tipocliente', 'idcliente')


class CuentaDeAhorro(forms.Form):
    codigocuenta = forms.IntegerField(required=True, label="Codigo de la cuenta")
    tasainteres = forms.IntegerField(required=True, label="Tasa de interes (%)")
    saldo = forms.DecimalField(required=True, label="Saldo")
    lstipoCliente = [(1,"Cliente individual"), (2, "Empresa")]
    tipocliente = forms.CharField(widget=forms.Select(choices=lstipoCliente))
    idcliente = forms.IntegerField(required=True, label="Cui del cliente o ID de la Empresa")

    class Meta:
        model = Cuentadeahorro
        fields = ('codigocuenta', 'tasainteres', 'saldo', 'tipocliente', 'idcliente')


class CuentaPlazoFijo(forms.Form):
    codigocuenta = forms.IntegerField(required=True, label="Codigo de la cuenta")
    tasainteres = forms.IntegerField(required=True, label="Tasa de interes (%)")
    periodotiempo = forms.IntegerField(required=True, label="Periodo de tiempo (# meses)")
    saldo = forms.DecimalField(required=True, label="Saldo")
    lstipoCliente = [(1,"Cliente individual"), (2, "Empresa")]
    tipocliente = forms.CharField(widget=forms.Select(choices=lstipoCliente))
    idcliente = forms.IntegerField(required=True, label="Cui del cliente o ID de la Empresa")

    class Meta:
        model = Cuentaplazofijo
        fields = ('codigocuenta', 'tasainteres', 'periodotiempo', 'saldo', 'tipocliente', 'idcliente')
