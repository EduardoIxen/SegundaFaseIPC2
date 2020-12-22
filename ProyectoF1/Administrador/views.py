from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
import MySQLdb

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
    form = Empresa()
    nombre = "Registro de Empresa"
    variables = {
        "form": form,
        "mensaje": nombre
    }
    if request.method == "POST":
        form = Empresa(data=request.POST)
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
            form = Empresa()
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
    #     db = MySQLdb.connect(host=host, user=user, password=contra, db=db_name, connect_timeout=5)
    #     cursor = db.cursor()
        #consulta = "SELECT * FROM Administrador WHERE usuario = '"+usuario+"' and contrasenia = '"+password+"'"
        admin = Administrador.objects.filter(usuario=usuario).filter(contrasenia=password).values_list()
        print(admin)
        if not admin:
            mensaje = "Usuario o contraseña incorrectos"
        else:
            mensaje = "Usuario logueado"
            return redirect('registrocliente', permanent=True)
        variables = {
            'mensaje': mensaje
        }

    return render(request, "adminlogin.html", variables)