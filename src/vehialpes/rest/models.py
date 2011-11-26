from django.db import models

class Taller(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    