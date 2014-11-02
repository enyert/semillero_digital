# -*- coding: utf8 -*-

__author__ = 'enyert'

from api.models import *

from rest_framework import serializers

class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro

class SemillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semilla
        depth = 1

class SemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semillero
        depth = 2

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        depth = 1

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        depth = 2