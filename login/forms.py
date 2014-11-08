# -*- coding: utf8 -*-
__author__ = 'enyert'

import re
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="Nombre de usuario")),
                                error_messages={ 'invalid': "Nombre de usuario inválido" })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="Correo Electrónico")))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Contraseña")))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Repetir contraseña")))

    def clean_username(self):
        user = User.objects.filter(username=self.cleaned_data['username'])
        if len(user) > 0:
            print "El nombre de usuario existe. Por favor introduzca uno diferente."
            raise forms.ValidationError("El nombre de usuario existe. Por favor introduzca uno diferente.")
        else:
            return self.cleaned_data['username']


    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            print "Las contraseñas no coinciden"
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return self.cleaned_data


class SearchForm(forms.Form):
    clave = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=60, placeholder="Introduzca las palabras clave", size="120")))

    def clean(self):
        return self.cleaned_data

class CrearSemilleroForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100, placeholder="Nombre del semillero", size="120")))
    direccion = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=350, placeholder="Descripción del semillero", size="120")))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=False, max_length=30, placeholder="Correo Electrónico", size="120")))
    tel_local = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=100, placeholder="Teléfono local", size="120")))
    tel_movil = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=100, placeholder="Celular", size="120")))

    def clean(self):
        return self.cleaned_data