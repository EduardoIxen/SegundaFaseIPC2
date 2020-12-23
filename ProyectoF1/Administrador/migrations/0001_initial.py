# Generated by Django 3.1.4 on 2020-12-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('idadministrador', models.AutoField(db_column='idAdministrador', primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clienteindividual',
            fields=[
                ('cui', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='CUI')),
                ('nit', models.CharField(max_length=20, verbose_name='NIT')),
                ('nombrecompleto', models.CharField(db_column='nombreCompleto', max_length=50, verbose_name='Nombre Completo')),
                ('fechanacimiento', models.DateField(db_column='fechaNacimiento', verbose_name='Fecha de nacimiento (Año-mes-dia)')),
                ('usuario', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'clienteindividual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.AutoField(db_column='idEmpresa', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('nombrecomercial', models.CharField(db_column='nombreComercial', max_length=50, verbose_name='Nombre Comercial')),
                ('nombrerepresentantelegal', models.CharField(db_column='nombreRepresentanteLegal', max_length=50, verbose_name='Nombre del Representante Legal')),
                ('usuario', models.CharField(max_length=50, verbose_name='Nombre de Usuario')),
                ('contrasenia', models.CharField(max_length=100, verbose_name='Contraseña')),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoempresa',
            fields=[
                ('idtipoempresa', models.AutoField(db_column='idTipoEmpresa', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tipoempresa',
                'managed': False,
            },
        ),
    ]
