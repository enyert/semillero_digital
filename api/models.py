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
    def generateURL(self, filename):
        return '/'.join(['semillas', 'avatars', self.user.username, filename])

    user = models.OneToOneField(User)
    rol = models.CharField(max_length=3, choices=ROLES)
    creada = models.DateTimeField(auto_now_add=True)
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_amigos = models.ManyToManyField("self", symmetrical=False, null=True, blank=True)
    puntos = models.IntegerField(default=0)
    logros_completados = models.ManyToManyField(Logro, blank=True, null=True)
    profile_image = models.ImageField(upload_to=generateURL, null=True, blank=True)

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
    #descripcion = models.TextField(max_length=350)
    creado = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(Semilla)
    actividades = models.ManyToManyField(Actividad, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    tel_local = models.CharField(max_length=20, blank=True, null=True)
    tel_movil = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    puntuacion = models.IntegerField(default=0)
    facebook_url = models.CharField(max_length=100, blank=True)
    twitter_url = models.CharField(max_length=100, blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    lista_semillas = models.ManyToManyField(Semilla, related_name="Semillas", blank=True, null=True)

    def __unicode__(self):
        return "Semillero: " + self.nombre + " - Creado por: " + self.creador.user.username

    class Meta:
        verbose_name_plural = "Semilleros"


class Evento(models.Model):
    def generateURL(self, filename):
        return '/'.join(['img', 'eventos', self.creador.user.username, filename])

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=350)
    creador = models.ForeignKey(Semilla)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    semillero = models.ForeignKey(Semillero, null=True, blank=True)
    audiencia = models.CharField(max_length=4, choices=AUDIENCIA_CHOICES)
    creado = models.DateTimeField()
    actividades = models.ManyToManyField(Actividad)
    puntuacion = models.IntegerField()
    #imagen_promo = models.ImageField(upload_to=generateURL, null=True, blank=True)

    def __unicode__(self):
        return "Evento: " + self.nombre + " - Creado por: " + self.creador.user.username

    class Meta:
        verbose_name_plural = "Eventos"