from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "login.html")

def registroCliente(request):
    return render(request, "registroCliente.html")

def transferencia(request):
    return render(request, "transferencia.html")

def pagoTarjeta(request):
    return render(request, "pagoTarjeta.html")

def preautorizacionCheque(request):
    return render(request, "preautorizacionCheque.html")

def prestamo(request):
    return render(request, "prestamo.html")

def estadoDeCeunta(request):
    return render(request, "estadoDeCuenta.html")

def pagoServicio(request):
    return render(request, "pagoservicio.html")