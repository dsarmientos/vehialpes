'''
Created on 25/11/2011

@author: Daniel Sarmiento <d.sarmiento85@uniandes.edu.co>
'''

from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
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
        resource_name = 'cliente'

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
    vehiculo = tastypie.fields.ForeignKey('rest.api.VehiculoResource', 'vehiculo')
    class Meta:
        queryset = Mantenimiento.objects.all()

class ServicioResource(ModelResource):
    class Meta:
        queryset = Servicio.objects.all()

class VehiculoResource(ModelResource):
    cliente = tastypie.fields.ForeignKey(ClienteResource, 'cliente', full=True)
    class Meta:
        queryset = Vehiculo.objects.all()
        filtering = {
            "placa": ALL,
        }


class RepuestoResource(ModelResource):
    class Meta:
        queryset = Repuesto.objects.all()

class CitaResource(ModelResource):
    vehiculo = tastypie.fields.ForeignKey('rest.api.VehiculoResource', 'vehiculo', full=True)
    taller = tastypie.fields.ForeignKey('rest.api.TallerResource', 'taller', full=True)
    tipo_transporte_entrega = tastypie.fields.ForeignKey('rest.api.TipoTransporteResource', 'tipo_transporte_entrega', full=True)
    tipo_transporte_recepcion = tastypie.fields.ForeignKey('rest.api.TipoTransporteResource', 'tipo_transporte_recepcion', full=True)
    class Meta:
        queryset = Cita.objects.all()
        filtering = {
            "taller": ALL_WITH_RELATIONS,
            "vehiculo": ALL_WITH_RELATIONS
        }

class TipoTransporteResource(ModelResource):
    class Meta:
        queryset = TipoTransporte.objects.all()