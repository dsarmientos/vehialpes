from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest.models import PicoYPlaca, Mantenimiento, Vehiculo
from django.utils import simplejson

def main(request):
    return render_to_response('index.html')

def picoyplaca(request, placa):
    if request.method == 'GET':
        ultimo_digito = int(placa[-1])
        pico_y_placa = PicoYPlaca.objects.filter(ultimo_digito=ultimo_digito)
        dias = [pp.dia_semana for pp in pico_y_placa]
        json = simplejson.dumps({'dias':dias})
        return HttpResponse(json, mimetype='application/json')
    return HttpResponse(status=400)

def ingreso_post_venta(request):
    if request.method == 'GET':
        mantenimientos = Mantenimiento.objects.all()
        total = sum([m.precio for m in mantenimientos])
        total = str(total)
        json = simplejson.dumps({'total':total})
        return HttpResponse(json, mimetype='application/json')
    return HttpResponse(status=400)

def ingreso_venta_vehiculos(request):
    if request.method == 'GET':
        vehiculos = Vehiculo.objects.all()
        total = sum([v.precio_venta for v in vehiculos if v.precio_venta])
        total = str(total)
        json = simplejson.dumps({'total':total})
        return HttpResponse(json, mimetype='application/json')
    return HttpResponse(status=400)