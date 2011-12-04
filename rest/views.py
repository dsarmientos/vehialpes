from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest.models import PicoYPlaca
from django.utils import simplejson

def main(request):
    return render_to_response('index.html')

def picoyplaca(request, placa):
    ultimo_digito = int(placa[-1])
    pico_y_placa = PicoYPlaca.objects.filter(ultimo_digito=ultimo_digito)
    dias = [pp.dia_semana for pp in pico_y_placa]
    json = simplejson.dumps({'dias':dias})
    return HttpResponse(json, mimetype='application/json')
