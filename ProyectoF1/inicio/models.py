# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    idadministrador = models.AutoField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'administrador'


class Clienteindividual(models.Model):
    cui = models.BigIntegerField(primary_key=True)
    nit = models.CharField(max_length=20)
    nombrecompleto = models.CharField(db_column='nombreCompleto', max_length=50)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'clienteindividual'


class Cuentadeahorro(models.Model):
    codigocuenta = models.BigIntegerField(db_column='codigoCuenta', primary_key=True)  # Field name made lowercase.
    tasainteres = models.IntegerField(db_column='tasaInteres')  # Field name made lowercase.
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cuentadeahorro'


class Cuentamonetaria(models.Model):
    codigocuenta = models.BigIntegerField(db_column='codigoCuenta', primary_key=True)  # Field name made lowercase.
    montopormanejo = models.DecimalField(db_column='montoPorManejo', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cuentamonetaria'


class Cuentaplazofijo(models.Model):
    codigocuenta = models.BigIntegerField(db_column='codigoCuenta', primary_key=True)  # Field name made lowercase.
    tasainteres = models.IntegerField(db_column='tasaInteres')  # Field name made lowercase.
    periododetiempo = models.IntegerField(db_column='periodoDeTiempo')  # Field name made lowercase.
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cuentaplazofijo'


class Detalleclientecuenta(models.Model):
    codigodetalle = models.AutoField(db_column='codigoDetalle', primary_key=True)  # Field name made lowercase.
    codigocliente = models.ForeignKey(Clienteindividual, models.DO_NOTHING, db_column='codigoCliente', blank=True, null=True)  # Field name made lowercase.
    idempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    codigocuentamonetaria = models.ForeignKey(Cuentamonetaria, models.DO_NOTHING, db_column='codigoCuentaMonetaria', blank=True, null=True)  # Field name made lowercase.
    codigocuentaahorro = models.ForeignKey(Cuentadeahorro, models.DO_NOTHING, db_column='codigoCuentaAhorro', blank=True, null=True)  # Field name made lowercase.
    codigocuentaplazofijo = models.ForeignKey(Cuentaplazofijo, models.DO_NOTHING, db_column='codigoCuentaPlazoFijo', blank=True, null=True)  # Field name made lowercase.
    estaactiva = models.IntegerField(db_column='estaActiva')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalleclientecuenta'


class Empresa(models.Model):
    idempresa = models.BigAutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    idtipoempresa = models.ForeignKey('Tipoempresa', models.DO_NOTHING, db_column='idTipoEmpresa')  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=50)  # Field name made lowercase.
    nombrerepresentantelegal = models.CharField(db_column='nombreRepresentanteLegal', max_length=50)  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'empresa'


class Tipoempresa(models.Model):
    idtipoempresa = models.AutoField(db_column='idTipoEmpresa', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # return '{} {}'.format(self.idtipoempresa, self.nombre)
        return '{}'.format(self.nombre)
    
    class Meta:
        managed = False
        db_table = 'tipoempresa'
