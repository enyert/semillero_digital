# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User


TIPOS_CHOICES = (('DEP', 'Deportiva'), ('CUL', 'Cultural'),)
AUDIENCIA_CHOICES = (('CHIL','Niños'), ('ADOL', 'Adolescentes'), ('VIEJ', 'Adultos mayores'), ('TODO', 'Todos'),)
ROLES = (('INS', 'Instructor'), ('COM', 'Miembro Comunidad'),)


class Logro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=350)
    puntos = models.IntegerField()

class Semilla(models.Model):
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to='img/', null=True)
    rol = models.CharField(max_length=3, choices=ROLES)
    creada = models.DateTimeField()
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_amigos = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)
    puntos = models.IntegerField()
    logros_completados = models.ManyToManyField()
    logros_no_completados = models.ManyToManyField()


    def __str__(self):
        return "%s's profile" % self.user


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=350)
    tipo = models.CharField(max_length=3, choices=TIPOS_CHOICES)
    creada = models.DateTimeField()


class Semillero(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=350)
    creado = models.DateTimeField()
    actividades = models.ManyToManyField(Actividad)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tel_local = models.CharField(max_length=20)
    tel_movil = models.CharField(max_length=20)
    correo = models.EmailField()
    puntuacion = models.IntegerField()
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_semillas = models.ManyToManyField(Semilla)


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=350)
    creador = models.ForeignKey(Semilla)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    semilleros = models.ForeignKey(Semillero, null=True)
    audiencia = models.CharField(max_length=4, choices=AUDIENCIA_CHOICES)
    creado = models.DateTimeField()
    actividades = models.ManyToManyField(Actividad)
    votos = models.IntegerField()
    puntuacion = models.IntegerField()