# -*- coding: utf8 -*-

from login.forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from api.models import Semilla, Semillero


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print "form.is_valid()"
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            seed = Semilla(user=user, rol='COM', puntos=0)
            seed.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, { 'form': form })

    return render_to_response('registration/register.html', variables,)

def register_success(request):
    return render_to_response(
        'registration/success.html'
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/index')

@login_required
def home(request):
    return render_to_response('home.html', RequestContext(request, { 'user', request.user }),)

@login_required
def basicSearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        clave = request.POST.get("clave", "")

        semillas = Semilla.objects.filter(Q(user__username__contains=clave)
                                          | Q(user__email__contains=clave))

        semilleros = Semillero.objects.filter(Q(creador__user__username__contains=clave)
                                            | Q(creador__user__email__contains=clave)
                                            | Q(nombre__contains=clave))
        variables = RequestContext(request, { 'semillas':semillas, 'semilleros':semilleros })

        return render_to_response('results.html', variables,)
    else:
        form = SearchForm()

    variables = RequestContext(request, { 'form': form })

    return render_to_response('search.html', variables,)

@login_required
def crearSemillero(request):
    if request.method == 'POST':
        username = request.user.username
        semilla = Semilla.objects.filter(user__username = username)[0]
        form = CrearSemilleroForm(request.POST)
        nombre = request.POST.get("nombre", "")
        direccion = request.POST.get("direccion", "")
        correo = request.POST.get("email", "")
        tel_local = request.POST.get("tel_local", "")
        tel_movil = request.POST.get("tel_movil", "")

        semillero = Semillero(nombre=nombre, direccion=direccion, creador=semilla, correo=correo, tel_local=tel_local,
                              tel_movil=tel_movil, puntuacion=0)
        semillero.save()
        return HttpResponseRedirect('/register/success/')
    else:
        form = CrearSemilleroForm()

    variables = RequestContext(request, { 'form' : form })

    return render_to_response('crearSemillero.html', variables,)

def index(request):
    return render_to_response('index.html', RequestContext(request, {  }))