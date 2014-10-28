# -*- coding: utf8 -*-

__author__ = 'enyert'

from api.models import *

from rest_framework import serializers

class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro
        fields = ('id', 'nombre', 'descripcion', 'puntos')



