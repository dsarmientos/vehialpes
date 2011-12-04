# vim: set fileencoding=utf-8

from django.contrib import admin
from rest.models import (Cliente, Ciudad, Cita, Servicio, Repuesto,
                         TipoTransporte, Consumible, Evidencia,
                         Mantenimiento, Vehiculo, Taller, PicoYPlaca)

models = [Cliente, Ciudad, Cita, Servicio, Repuesto, TipoTransporte,
          Consumible, Evidencia, Mantenimiento, Vehiculo, Taller, PicoYPlaca]

for model in models:
    admin.site.register(model)

