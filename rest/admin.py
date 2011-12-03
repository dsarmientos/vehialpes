# vim: set fileencoding=utf-8

from django.contrib import admin
from rest.models import Cliente, Ciudad, Servicio, Taller

models = [Cliente, Ciudad, Servicio, Taller]

for model in models:
    admin.site.register(model)

