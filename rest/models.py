from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

class Cita(models.Model):
    vehiculo = models.ForeignKey('Vehiculo')
    taller = models.ForeignKey('Taller')
    tipo_transporte_entrega = models.ForeignKey('TipoTransporte', related_name='+')
    tipo_transporte_recepcion = models.ForeignKey('TipoTransporte', related_name='+')
    fecha = models.DateTimeField()
    
    def __unicode__(self):
        return '-'.join((unicode(self.fecha), self.vehiculo.placa))
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    cedula = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)
    ciudad = models.ForeignKey('Ciudad')

    def __unicode__(self):
        return self.nombre


class Consumible(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(null=True, max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.nombre


class Evidencia(models.Model):
    titulo = models.CharField(max_length=80)
    observaciones = models.TextField(blank=True)
    media = models.URLField(verify_exists=False, null=True)

    def __unicode__(self):
        return self.media


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

    def __unicode__(self):
        return '-'.join((unicode(self.taller.nombre), self.vehiculo.placa))

class PicoYPlaca(models.Model):
    DIA_LUNES = 'L'
    DIA_MARTES = 'M'
    DIA_MIERCOLES = 'X'
    DIA_JUEVES = 'J'
    DIA_VIERNES = 'V'
    DIA_SABADO = 'S'
    DIA_DOMINGO = 'D'
    DIA_CHOICES = (
        (DIA_LUNES, 'Lunes'),
        (DIA_MARTES, 'Martes'),
        (DIA_MIERCOLES, 'Miercoles'),
        (DIA_JUEVES, 'Jueves'),
        (DIA_VIERNES, 'Viernes'),
        (DIA_SABADO, 'Sabado'),
        (DIA_DOMINGO, 'Domingo'),
    )
    ultimo_digito = models.IntegerField(unique=True)
    dia_semana = models.CharField(choices=DIA_CHOICES, max_length='1')

    def __unicode__(self):
        return '%d-%s' % (self.ultimo_digito, self.dia_semana)

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

class Taller(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField(blank=True)
    rating = models.IntegerField(default=0)
    ciudad = models.ForeignKey('Ciudad')
    servicios = models.ManyToManyField('Servicio')

    def __unicode__(self):
        return self.nombre

class Vehiculo(models.Model):
    placa = models.CharField(max_length=6)
    cliente = models.ForeignKey('Cliente')
    modelo = models.IntegerField()
    foto = models.URLField(verify_exists=False, )
    linea = models.CharField(max_length=80, null=True)
    color = models.CharField(max_length=80, null=True)
    tipo_caja = models.CharField(max_length=10, null=True)
    motor = models.CharField(max_length=10, null=True)
    marca = models.CharField(max_length=100, default='Marca X', null=True)
    fecha_compra = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.placa

class Repuesto(models.Model):
    nombre = models.CharField(max_length=200)
    referencia = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(null=True, max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.nombre


class TipoTransporte(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre
