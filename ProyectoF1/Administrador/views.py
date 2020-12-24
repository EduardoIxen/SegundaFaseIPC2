from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
import MySQLdb

from .models import Empresa

host = 'localhost'
db_name = 'Proyecto'
user = 'root'
contra = 'admin'
puerto = 3306

# Create your views here.
def registroCliente(request):
    form = Cliente()
    nombre = "Registro de cliente individual"
    variables = {
        "form":form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = Cliente(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            cui = datos.get('cui')
            nit = datos.get('nit')
            nombreCompleto = datos.get('nombrecompleto')
            fechaNacimiento = datos.get('fechanacimiento')
            usuario = datos.get('usuario')
            contrasenia = datos.get('contrasenia')
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            cursor = db.cursor()
            consulta = "INSERT INTO ClienteIndividual VALUES("+str(cui)+",'"+nit+"','"+nombreCompleto+"', '"+str(fechaNacimiento)+"', '"+usuario+"', '"+contrasenia+"')"
            #print(consulta)
            cursor.execute(consulta)
            db.commit()
            cursor.close()
            nombre = f"Usuario {nombreCompleto} registrado de manera correcta"
            form = Cliente()
            variables = {
                "form": form,
                "mensaje": nombre
            }
        else:
            nombre = "Error de registro, intente de nuevo"
            variables = {
                "form":form,
                "mensaje":nombre
            }

    return render(request, 'registroCliente.html', variables)

def registroEmpresa(request):
    form = Empresaa()
    nombre = "Registro de Empresa"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = Empresaa(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            idTipoEmpresa = datos.get('idtipoempresa')
            print(type(idTipoEmpresa.idtipoempresa), "tipooo")
            nombre = datos.get('nombre')
            nombreComercial = datos.get('nombrecomercial')
            nombreRepresentanteLegal = datos.get('nombrerepresentantelegal')
            usuario = datos.get('usuario')
            contrasenia = datos.get('contrasenia')
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            cursor = db.cursor()
            consulta = "INSERT INTO Empresa(idTipoEmpresa, nombre, nombreComercial, nombreRepresentanteLegal, usuario, contrasenia) VALUES(" + str(
                idTipoEmpresa.idtipoempresa) + ",'" + nombre + "','" + nombreComercial + "', '" + nombreRepresentanteLegal + "', '" + usuario + "', '" + contrasenia + "')"
            print(consulta)
            cursor.execute(consulta)
            db.commit()
            cursor.close()
            nombre = f"Empresa {nombreComercial} registrada de manera correcta"
            form = Empresaa()
            variables = {
                "form": form,
                "mensaje": nombre
            }
        else:
            nombre = "Error de registro, intente de nuevo"
            variables = {
                "form": form,
                "mensaje": nombre
            }
    return render(request, 'registroEmpresa.html', variables)

def loginAdmin(request):
    mensaje = ""
    variables = {
        'mensaje': mensaje
    }
    if request.method == "POST":
        usuario = request.POST['usuariolog']
        password = request.POST['passwordlog']
        print(usuario)
        print(password)
        #consulta = "SELECT * FROM Administrador WHERE usuario = '"+usuario+"' and contrasenia = '"+password+"'"
        admin = Administrador.objects.filter(usuario=usuario).filter(contrasenia=password).values_list()
        if not admin:
            mensaje = "Usuario o contraseña incorrectos"
        else:
            usrL = admin[0][1]
            dicSession = {
                'usuario':usrL
            }
            request.session['datos'] = dicSession
            return redirect('registrocliente')
    variables = {
        'mensaje': mensaje
    }

    return render(request, "adminlogin.html", variables)

def logout(request):
    dic = request.session['datos']
    nombre = dic.get('nombre')
    print("nombreeeee en admin", nombre)
    return redirect('loginadmin')

def addCuentaMonetaria(request):
    form = CuentaMonetaria()
    mensaje = ""
    variables = {
        'form':form,
        'mensaje':mensaje
    }
    if request.method == "POST":
        form = CuentaMonetaria(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigoCuenta = datos.get('codigocuenta')
            montoPorManejo = datos.get('montopormanejo')
            saldo = datos.get('saldo')
            tipoCliente = datos.get('tipocliente')
            idCliente = datos.get('idcliente')

            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)

            cursor = db.cursor()
            cursor2 = db.cursor()
            consulta = "INSERT INTO CuentaMonetaria VALUES(" + str(codigoCuenta) + "," + str(
                montoPorManejo) + "," + str(saldo) + ")"
            print(consulta)
            cursor.execute(consulta)
            db.commit()
            cursor.close()
            if tipoCliente.strip() == "1": #persona individual
                cliente = Clienteindividual.objects.filter(cui=idCliente).values_list()
                if not cliente:
                    mensaje = "El cliente no existe"
                    form = CuentaMonetaria()
                    variables = {
                        'mensaje':mensaje,
                        'form':form
                    }
                else:
                    consulta2 = "INSERT INTO DetalleClienteCuenta(codigoCliente, codigoCuentaMonetaria, estaActiva) VALUES("+str(
                        idCliente)+", "+str(codigoCuenta)+", "+str(True)+")"
                    print(consulta2)
                    cursor2.execute(consulta2)
                    db.commit()
                    cursor2.close()
                    form = CuentaMonetaria()
                    mensaje = "Cuenta creada correctamente"
                    variables = {
                        'form': form,
                        'mensaje': mensaje
                    }
            elif tipoCliente.strip() == "2":
                cliente = Empresa.objects.filter(idempresa=idCliente).values_list()
                if not cliente:
                    mensaje = "El cliente no existe"
                    form = CuentaMonetaria()
                    variables = {
                        'mensaje': mensaje,
                        'form': form
                    }
                else:
                    consulta2 = "INSERT INTO DetalleClienteCuenta(idEmpresa, codigoCuentaMonetaria, estaActiva) VALUES(" + str(
                        idCliente) + ", " + str(codigoCuenta) + ", " + str(True) + ")"
                    print(consulta2)
                    cursor2.execute(consulta2)
                    db.commit()
                    cursor2.close()
                    form = CuentaMonetaria()
                    mensaje = "Cuenta creada correctamente"
                    variables = {
                        'form': form,
                        'mensaje': mensaje
                    }
        else:
            mensaje = "Error de registro de cuenta"
            variables = {
                'form':form,
                'mensaje':mensaje
            }

    return render(request, "addCuentaMonetaria.html", variables)

def addCuentaDeAhorro(request):
    form = CuentaDeAhorro()
    mensaje = ''
    variables = {
        'mensaje': mensaje,
        'form': form
    }
    if request.method == "POST":
        form = CuentaDeAhorro(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigoCuenta = datos.get('codigocuenta')
            tasainteres = datos.get('tasainteres')
            saldo = datos.get('saldo')
            tipoCliente = datos.get('tipocliente')
            idCliente = datos.get('idcliente')
            print(f"{type(tipoCliente)}, id {type(idCliente)}")
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            cursor = db.cursor()
            cursor2 = db.cursor()
            cuenta1 = Cuentadeahorro.objects.filter(codigocuenta=codigoCuenta).values_list()
            cuenta2 = Cuentaplazofijo.objects.filter(codigocuenta=codigoCuenta).values_list()
            cuenta3 = Cuentadeahorro.objects.filter(codigocuenta=codigoCuenta).values_list()
            pasa = False
            if not cuenta1:
                if not cuenta2:
                    if not cuenta3:
                       pasa = True
            if pasa:
                consulta = "INSERT INTO CuentaDeAhorro VALUES(" + str(codigoCuenta) + "," + str(
                    tasainteres) + "," + str(saldo) + ")"
                print(consulta)
                cursor.execute(consulta)
                db.commit()
                cursor.close()
                if tipoCliente.strip() == "1": #persona individual
                    cliente = Clienteindividual.objects.filter(cui=idCliente).values_list()
                    if not cliente:
                        mensaje = "El cliente no existe"
                        form = CuentaDeAhorro()
                        variables = {
                            'mensaje':mensaje,
                            'form':form
                        }
                    else:
                        consulta2 = "INSERT INTO DetalleClienteCuenta(codigoCliente, codigoCuentaAhorro, estaActiva) VALUES("+str(
                            idCliente)+", "+str(codigoCuenta)+", "+str(True)+")"
                        print(consulta2)
                        cursor2.execute(consulta2)
                        db.commit()
                        cursor2.close()
                        form = CuentaDeAhorro()
                        mensaje = "Cuenta creada correctamente"
                        variables = {
                            'form': form,
                            'mensaje': mensaje
                        }
                elif tipoCliente.strip() == "2":
                    cliente = Empresa.objects.filter(idempresa=idCliente).values_list()
                    if not cliente:
                        mensaje = "El cliente no existe"
                        form = CuentaDeAhorro()
                        variables = {
                            'mensaje': mensaje,
                            'form': form
                        }
                    else:
                        consulta2 = "INSERT INTO DetalleClienteCuenta(idEmpresa, codigoCuentaAhorro, estaActiva) VALUES(" + str(
                            idCliente) + ", " + str(codigoCuenta) + ", " + str(True) + ")"
                        print(consulta2)
                        cursor2.execute(consulta2)
                        db.commit()
                        cursor2.close()
                        form = CuentaDeAhorro()
                        mensaje = "Cuenta creada correctamente"
                        variables = {
                            'form': form,
                            'mensaje': mensaje
                        }
            else:
                mensaje = "El codigo de la cuenta ya existe"
                form = CuentaDeAhorro()
                variables = {
                    'mensaje': mensaje,
                    'form': form
                }
        else:
            mensaje = "Error de registro de cuenta"
            variables = {
                'form':form,
                'mensaje':mensaje
            }

    return render(request, "addCuentaAhorro.html", variables)

def addCuentaPlazoFijo(request):
    form = CuentaPlazoFijo()
    mensaje = ''
    variables = {
        'mensaje': mensaje,
        'form': form
    }
    if request.method == "POST":
        form = CuentaPlazoFijo(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            codigoCuenta = datos.get('codigocuenta')
            tasainteres = datos.get('tasainteres')
            periodoTiempo = datos.get('periodotiempo')
            saldo = datos.get('saldo')
            tipoCliente = datos.get('tipocliente')
            idCliente = datos.get('idcliente')
            print(f"{type(tipoCliente)}, id {type(idCliente)}")
            db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
            cursor = db.cursor()
            cursor2 = db.cursor()
            consulta = "INSERT INTO CuentaPlazoFijo VALUES(" + str(codigoCuenta) + "," + str(
                tasainteres) + ","+str(periodoTiempo)+" ," + str(saldo) + ")"
            print(consulta)
            cursor.execute(consulta)
            db.commit()
            cursor.close()
            if tipoCliente.strip() == "1":  # persona individual
                cliente = Clienteindividual.objects.filter(cui=idCliente).values_list()
                if not cliente:
                    mensaje = "El cliente no existe"
                    form = CuentaDeAhorro()
                    variables = {
                        'mensaje': mensaje,
                        'form': form
                    }
                else:
                    consulta2 = "INSERT INTO DetalleClienteCuenta(codigoCliente, codigoCuentaPlazoFijo, estaActiva) VALUES(" + str(
                        idCliente) + ", " + str(codigoCuenta) + ", " + str(True) + ")"
                    print(consulta2)
                    cursor2.execute(consulta2)
                    db.commit()
                    cursor2.close()
                    form = CuentaDeAhorro()
                    mensaje = "Cuenta creada correctamente"
                    variables = {
                        'form': form,
                        'mensaje': mensaje
                    }
            elif tipoCliente.strip() == "2":
                cliente = Empresa.objects.filter(idempresa=idCliente).values_list()
                if not cliente:
                    mensaje = "El cliente no existe"
                    form = CuentaDeAhorro()
                    variables = {
                        'mensaje': mensaje,
                        'form': form
                    }
                else:
                    consulta2 = "INSERT INTO DetalleClienteCuenta(idEmpresa, codigoCuentaPlazoFijo, estaActiva) VALUES(" + str(
                        idCliente) + ", " + str(codigoCuenta) + ", " + str(True) + ")"
                    print(consulta2)
                    cursor2.execute(consulta2)
                    db.commit()
                    cursor2.close()
                    form = CuentaDeAhorro()
                    mensaje = "Cuenta creada correctamente"
                    variables = {
                        'form': form,
                        'mensaje': mensaje
                    }
        else:
            mensaje = "Error de registro de cuenta"
            variables = {
                'form': form,
                'mensaje': mensaje
            }
    return render(request, "addCuentaPlazoFijo.html", variables)