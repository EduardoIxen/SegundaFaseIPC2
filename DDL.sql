create database Proyecto;
use Proyecto;

create table ClienteIndividual(
	cui bigint primary key not null,
    nit varchar(20) not null,
    nombreCompleto varchar(50) not null,
    fechaNacimiento date not null,
    usuario varchar(50) not null,
    contrasenia varchar(100) not null
);
create table TipoEmpresa(
	idTipoEmpresa int primary key auto_increment not null,
    nombre varchar(50) not null,
    descripcion varchar(255) null
);
create table Empresa(
	idEmpresa bigint primary key auto_increment not null,
    idTipoEmpresa int not null,
    nombre varchar(50) not null,
    nombreComercial varchar(50) not null,
    nombreRepresentanteLegal varchar(50) not null,
    usuario varchar(50) not null,
    contrasenia varchar(100) not null,
    foreign key(idTipoEmpresa) references TipoEmpresa(idTipoEmpresa)
);
create table Administrador(
	idAdministrador int primary key auto_increment not null,
    usuario varchar(100) not null,
    contrasenia varchar(100) not null
);
create table CuentaMonetaria(
	codigoCuenta bigint primary key not null,
    montoPorManejo numeric(5,2),
    saldo numeric(15,2) not null
);

create table CuentaDeAhorro(
	codigoCuenta bigint primary key not null,
    tasaInteres int not null,
    saldo numeric(15,2) not null
);
create table CuentaPlazoFijo(
	codigoCuenta bigint primary key not null,
    tasaInteres int not null,
    periodoDeTiempo int not null,
    saldo numeric(15,2) not null
);

create table DetalleClienteCuenta(
	codigoDetalle int not null primary key auto_increment,
	codigoCliente bigint null,
    idEmpresa bigint null,
    codigoCuentaMonetaria bigint null,
    codigoCuentaAhorro bigint null,
    codigoCuentaPlazoFijo bigint null,
    estaActiva boolean not null,
    foreign key(codigoCliente) references ClienteIndividual(cui),
    foreign key(idEmpresa) references Empresa(idEmpresa),
    foreign key(codigoCuentaMonetaria) references CuentaMonetaria(codigoCuenta),
    foreign key(codigoCuentaAhorro) references CuentaDeAhorro(codigoCuenta),
    foreign key(codigoCuentaPlazoFijo) references CuentaPlazoFijo(codigoCuenta)
);
create table Chequera(
	codigoChequera int primary key auto_increment ,
    cantidadDeCheques numeric(2,0) not null,
    codigoCuenta bigint not null,
    foreign key(codigoCuenta) references CuentaMonetaria(codigoCuenta)
);

create table Cheque(
	numeroCheque int primary key,
    codigoChequera int not null,
    foreign key(codigoChequera) references Chequera(codigoChequera)
);
create table AutorizacionCheque(
	numeroCheque int not null,
    cui bigint not null,
    codigoCuenta bigint not null,
    primary key(numeroCheque, cui, codigoCuenta),
    foreign key(numeroCheque) references Cheque(numeroCheque),
    foreign key(cui) references ClienteIndividual(cui),
    foreign key(codigoCuenta) references CuentaMonetaria(codigoCuenta)
);
create table Planilla(
	codigoPlanilla int primary key auto_increment,
    periodoPago numeric(2,0) not null,
    idEmpresa bigint not null,
    foreign key(idEmpresa) references Empresa(idEmpresa)
);
create table EmpleadoProveedor(
	codigoEmpleado bigint,
    codigoPlanilla int,
    montoPagar numeric(10,2) not null,
	codigoCuentaMonetaria bigint null,
    codigoCuentaAhorro bigint null,
    codigoCuentaPlazoFijo bigint null,
    primary key(codigoEmpleado, codigoPlanilla),
    foreign key(codigoPlanilla) references Planilla(CodigoPlanilla),
	foreign key(codigoCuentaMonetaria) references CuentaMonetaria(codigoCuenta),
    foreign key(codigoCuentaAhorro) references CuentaDeAhorro(codigoCuenta),
    foreign key(codigoCuentaPlazoFijo) references CuentaPlazoFijo(codigoCuenta)
);
create table Prestamo(
	codigoPrestamo int primary key auto_increment,
    montoRequerido numeric(15,2) not null,
    modalidadAPagar numeric(2,0) not null,
    codigoCliente bigint,
    idEmpresa bigint,
    foreign key(codigoCliente) references ClienteIndividual(cui),
    foreign key(idEmpresa) references Empresa(idEmpresa)
);

insert into TipoEmpresa(nombre, descripcion) values('Sociedad anonima', 'Descripcion pendiente');
insert into TipoEmpresa(nombre, descripcion) values('Compañia limitada', 'Descripcion pendiente');
insert into TipoEmpresa(nombre, descripcion) values('Empresa Individual', 'Descripcion pendiente');

insert into Administrador(usuario, contrasenia) value('admin','admin');