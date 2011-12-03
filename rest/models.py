from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

class Cita(models.Model):
    vehiculo = models.ForeignKey('Vehiculo')
    taller = models.ForeignKey('Taller')
    tipo_transporte_entrega = models.ForeignKey('TipoTransporte', related_name='+')
    tipo_transporte_recepcion = models.ForeignKey('TipoTransporte', related_name='+')
    fecha = models.DateTimeField()
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    cedula = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)
    ciudad = models.ForeignKey('Ciudad')


class Consumible(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(null=True, max_digits=8, decimal_places=2)

class Evidencia(models.Model):
    titulo = models.CharField(max_length=80)
    observaciones = models.TextField(blank=True)
    media = models.URLField(verify_exists=False, null=True)

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey('Vehiculo')
    taller = models.ForeignKey('Taller')
    diagnostico = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    recomendaciones = models.TextField(blank=True)
    consumibles = models.ManyToManyField('Consumible')
    respuestos = models.ManyToManyField('Repuesto')
    evidencias = models.ManyToManyField('Evidencia')
    cita = models.ForeignKey('Cita')


class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)


class Taller(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField(blank=True)
    rating = models.IntegerField(default=0)
    ciudad = models.ForeignKey('Ciudad')
    servicios = models.ManyToManyField('Servicio')


class Vehiculo(models.Model):
    placa = models.CharField(max_length=6)
    cliente = models.ForeignKey('Cliente')
    modelo = models.IntegerField()


class Repuesto(models.Model):
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(null=True, max_digits=8, decimal_places=2)


class TipoTransporte(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)