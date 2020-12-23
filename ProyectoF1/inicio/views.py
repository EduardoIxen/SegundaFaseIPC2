from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
# Create your views here.


def login(request):
    mensaje = ""
    variables = {
        'mensaje': mensaje,
        'usuariologueado': ''
    }
    if request.method == "POST":
        usuario = request.POST['usuariolog']
        password = request.POST['passwordlog']
        print(f"{usuario}, {password}")
        usuarioLogueado = Clienteindividual.objects.filter(usuario=usuario).filter(contrasenia=password).values_list()
        if not usuarioLogueado:
            mensaje = "Usuario o contraseña incorrectos"
        else:
            cuiL = usuarioLogueado[0][0]
            nitL = usuarioLogueado[0][1]
            nombreL = usuarioLogueado[0][2]
            fechaNacL = usuarioLogueado[0][3]
            usuarioL = usuarioLogueado[0][4]
            passL = usuarioLogueado[0][5]

            dicSession = {
                'cui': cuiL,
                'nit': nitL,
                'nombre': nombreL,
                'fechaNac': str(fechaNacL),
                'usuario': usuarioL,
                'pass': passL
            }
            request.session['datos'] = dicSession
            return redirect('infousr')
            #return HttpResponseRedirect(reverse('infousr'), render(request,'infousr.html', variables))
            #return redirect('infousr', variables)
            #return infoUsr(request, "infoUsr.html", variables)
            #return render(request, "infoUsr.html", context=variables)
        variables = {
            'mensaje': mensaje,
        }

    return render(request, "login.html", variables)

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

def base1(request):
    return render(request, "desdebase.html")

def infoUsr(request):
    diccSession = request.session['datos']
    return render(request, "infoUsr.html", diccSession)

def logout(request):
    request.session['datos'] = {}
    dic = request.session['datos']
    nombre = dic.get('nombre')
    print("nombreeeee", nombre)
    return HttpResponseRedirect(reverse('login'))
