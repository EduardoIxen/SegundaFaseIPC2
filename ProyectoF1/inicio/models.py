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
    cui = models.BigIntegerField(primary_key=True, verbose_name="CUI")
    nit = models.CharField(max_length=20, verbose_name="NIT")
    nombrecompleto = models.CharField(db_column='nombreCompleto', max_length=50, verbose_name="Nombre Completo")  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', verbose_name="Fecha de nacimiento (Año-mes-dia)")  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'clienteindividual'


class Empresa(models.Model):
    idempresa = models.AutoField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    idtipoempresa = models.ForeignKey('Tipoempresa', models.DO_NOTHING, db_column='idTipoEmpresa', verbose_name="Tipo Empresa")  # Field name made lowercase.
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=50, verbose_name="Nombre Comercial")  # Field name made lowercase.
    nombrerepresentantelegal = models.CharField(db_column='nombreRepresentanteLegal', max_length=50, verbose_name="Nombre del Representante Legal")  # Field name made lowercase.
    usuario = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    contrasenia = models.CharField(max_length=100, verbose_name="Contraseña")

    class Meta:
        managed = False
        db_table = 'empresa'



class Tipoempresa(models.Model):
    idtipoempresa = models.AutoField(db_column='idTipoEmpresa', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        #return '{} {}'.format(self.idtipoempresa, self.nombre)
        return '{}'.format(self.nombre)

    class Meta:
        managed = False
        db_table = 'tipoempresa'
