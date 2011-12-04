'''
Created on 25/11/2011

@author: Daniel Sarmiento <d.sarmiento85@uniandes.edu.co>
'''

from tastypie.resources import ModelResource
from tastypie.constants import ALL
import tastypie.fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from rest.models import *

class TallerResource(ModelResource):
    class Meta:
        queryset = Taller.objects.all()
        authentication = BasicAuthentication()
        authorization = Authorization()

class ClienteResource(ModelResource):
    class Meta:
        queryset = Cliente.objects.all()

class CiudadResource(ModelResource):
    class Meta:
        queryset = Ciudad.objects.all()
        authentication = BasicAuthentication()
        authorization = Authorization()
        filtering = {
            "nombre": ('exact', 'startswith',),
        }
    
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
        cliente = tastypie.fields.ForeignKey(ClienteResource, 'cliente')
        filtering = {
            "placa": ALL,
        }


class RepuestoResource(ModelResource):
    class Meta:
        queryset = Repuesto.objects.all()

class CitaResource(ModelResource):
    class Meta:
        queryset = Cita.objects.all()
        filtering = {
            "taller": ALL,
            "vehiculo": ALL
        }

class TipoTransporteResource(ModelResource):
    class Meta:
        queryset = TipoTransporte.objects.all()