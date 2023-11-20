# Generated by Django 3.2.4 on 2023-11-19 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro_cliente',
            fields=[
                ('idCliente', models.AutoField(db_column='id_cliente', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100)),
                ('aPaterno', models.CharField(db_column='aPaterno', max_length=100)),
                ('aMaterno', models.CharField(db_column='aMaterno', max_length=100)),
                ('correo', models.CharField(db_column='correo', max_length=100)),
                ('pswd_cliente', models.CharField(db_column='pswd_cliente', max_length=100)),
                ('genero', models.CharField(db_column='genero', max_length=100)),
                ('codigo', models.CharField(db_column='codigo', max_length=100)),
                ('fecha_compra', models.DateField(db_column='fecha_compra')),
            ],
            options={
                'db_table': 'registro_cliente',
            },
        ),
        migrations.CreateModel(
            name='tinaco',
            fields=[
                ('idTinaco', models.AutoField(db_column='id_tinaco', primary_key=True, serialize=False)),
                ('modelo', models.CharField(db_column='modelo', max_length=100)),
                ('capacidad', models.CharField(db_column='capacidad', max_length=100)),
            ],
            options={
                'db_table': 'tinaco',
            },
        ),
        migrations.CreateModel(
            name='tinaco_cliente',
            fields=[
                ('idRegistro', models.AutoField(db_column='id_registro', primary_key=True, serialize=False)),
                ('idCliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='api.registro_cliente')),
                ('idTinaco', models.ForeignKey(db_column='id_tinaco', on_delete=django.db.models.deletion.CASCADE, to='api.tinaco')),
            ],
            options={
                'db_table': 'tinacoHasCliente',
            },
        ),
        migrations.CreateModel(
            name='sesion',
            fields=[
                ('id_sesion', models.AutoField(db_column='id_sesion', primary_key=True, serialize=False)),
                ('estatus', models.CharField(db_column='status_sesion', max_length=100)),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='api.registro_cliente')),
            ],
            options={
                'db_table': 'sesion_estatus',
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id_click', models.AutoField(db_column='id_click', primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='fecha_click')),
                ('hora', models.TimeField(db_column='hora_click')),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='api.registro_cliente')),
            ],
            options={
                'db_table': 'clicks',
            },
        ),
    ]