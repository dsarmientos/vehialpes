from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import render_to_string

def main(request):
    return render_to_response('index.html')

def policy(request):
    xml = render_to_string('policy.html')
    return HttpResponse(xml, mimetype='application/xml')
