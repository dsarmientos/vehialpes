# vim: set fileencoding=utf-8

from django.contrib import admin
from rest.models import (Cliente, Ciudad, Cita, Servicio, Repuesto,
                         TipoTransporte, Consumible, Evidencia,
                         Mantenimiento, Vehiculo, Taller)

models = [Cliente, Ciudad, Cita, Servicio, Repuesto, TipoTransporte,
          Consumible, Evidencia, Mantenimiento, Vehiculo, Taller]

for model in models:
    admin.site.register(model)

