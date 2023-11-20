from django.db import models
from django.forms import DateField
from django import forms


# Create your models here.
class registro_cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,db_column='id_cliente')
    nombre = models.CharField(max_length=100, db_column='nombre')
    aPaterno = models.CharField(max_length=100, db_column='aPaterno')
    aMaterno = models.CharField(max_length=100, db_column='aMaterno')
    correo = models.CharField(max_length=100, db_column='correo')
    pswd_cliente = models.CharField(max_length=100, db_column='pswd_cliente')
    genero = models.CharField(max_length=100, db_column='genero')
    codigo = models.CharField(max_length=100, db_column='codigo')
    class Meta: 
        db_table='registro_cliente'

    

class tinaco(models.Model):
    idTinaco = models.AutoField(primary_key=True,db_column='id_tinaco')
    modelo = models.CharField(max_length=100, db_column='modelo')
    capacidad = models.CharField(max_length=100, db_column='capacidad')
    class Meta:
        db_table='tinaco'

class tinaco_cliente(models.Model):
    idRegistro = models.AutoField(primary_key=True,db_column='id_registro')
    idTinaco = models.ForeignKey(tinaco, on_delete=models.CASCADE, db_column='id_tinaco')
    idCliente = models.ForeignKey(registro_cliente, on_delete=models.CASCADE, db_column='id_cliente')
    class Meta:
        db_table='tinacoHasCliente'

class Click(models.Model):
    id_click = models.AutoField(primary_key=True, db_column='id_click')
    id_cliente = models.ForeignKey(registro_cliente, on_delete=models.CASCADE, db_column='id_cliente')
    fecha = models.DateField(db_column='fecha_click')
    hora = models.TimeField(db_column='hora_click')
    class Meta:
        db_table = 'clicks'

class sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True, db_column='id_sesion')
    id_cliente = models.ForeignKey(registro_cliente, on_delete=models.CASCADE, db_column='id_cliente')
    estatus = models.CharField(max_length=100, db_column='status_sesion')
    class Meta:
        db_table = 'sesion_estatus'