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

    def __unicode__(self):
        return "Logro: " + self.nombre + " - Puntuacion: " + str(self.puntos)

    class Meta:
        verbose_name_plural = "Logros"


class Semilla(models.Model):
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to='img/', null=True)
    rol = models.CharField(max_length=3, choices=ROLES)
    creada = models.DateTimeField()
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_amigos = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)
    puntos = models.IntegerField(default=0)
    logros_completados = models.ManyToManyField(Logro)

    def __unicode__(self):
        return "%s's profile" % self.user

    class Meta:
        verbose_name_plural = "Semillas"


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=350)
    tipo = models.CharField(max_length=3, choices=TIPOS_CHOICES)
    creada = models.DateTimeField()

    def __unicode__(self):
        return "Actividad: " + self.nombre + " - Tipo: " + self.tipo

    class Meta:
        verbose_name_plural = "Actividades"


class Semillero(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=350)
    creado = models.DateTimeField()
    creador = models.ForeignKey(Semilla)
    actividades = models.ManyToManyField(Actividad)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tel_local = models.CharField(max_length=20, blank=True, null=True)
    tel_movil = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField()
    puntuacion = models.IntegerField()
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_semillas = models.ManyToManyField(Semilla, related_name="Semillas")

    def __unicode__(self):
        return "Semillero: " + self.nombre + " - Creado por: " + self.creador.user.username

    class Meta:
        verbose_name_plural = "Semilleros"


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
    puntuacion = models.IntegerField()

    def __unicode__(self):
        return "Evento: " + self.nombre + " - Creado por: " + self.creador.user.username

    class Meta:
        verbose_name_plural = "Eventos"