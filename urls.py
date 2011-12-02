from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from rest.api import *

v1_api = Api(api_name='v1')
v1_api.register(ClienteResource())
v1_api.register(TallerResource())
v1_api.register(CiudadResource())
v1_api.register(ConsumibleResource())
v1_api.register(EvidenciaResource())
v1_api.register(MantenimientoResource())
v1_api.register(ServicioResource())
v1_api.register(VehiculoResource())
v1_api.register(RepuestoResource())

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'vehialpes.rest.views.main', name='home'),
     (r'^api/', include(v1_api.urls)),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
