'''
Created on 25/11/2011

@author: Daniel Sarmiento <d.sarmiento85@uniandes.edu.co>
'''
from tastypie.resources import ModelResource
from rest.models import Taller


class TallerResource(ModelResource):
    class Meta:
        queryset = Taller.objects.all()

