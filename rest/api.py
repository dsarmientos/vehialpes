'''
Created on 25/11/2011

@author: Daniel Sarmiento <d.sarmiento85@uniandes.edu.co>
'''
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from rest.models import *


class TallerResource(ModelResource):
    class Meta:
        queryset = Taller.objects.all()

class ClienteResource(ModelResource):
    class Meta:
        queryset = Cliente.objects.all()

class CiudadResource(ModelResource):
    class Meta:
        queryset = Ciudad.objects.all()

class ConsumibleResource(ModelResource):
    class Meta:
        queryset = Consumible.objects.all()

class EvidenciaResource(ModelResource):
    class Meta:
        queryset = Evidencia.objects.all()

class MantenimientoResource(ModelResource):
    class Meta:
        queryset = Mantenimiento.objects.all()

class ServicioResource(ModelResource):
    class Meta:
        queryset = Servicio.objects.all()

class VehiculoResource(ModelResource):
    class Meta:
        queryset = Vehiculo.objects.all()

class RepuestoResource(ModelResource):
    class Meta:
        queryset = Repuesto.objects.all()
