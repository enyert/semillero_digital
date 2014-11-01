from api.models import *
from rest_framework import viewsets
from api.serializers import *


class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer

class SemillaViewSet(viewsets.ModelViewSet):
    queryset = Semilla.objects.all()
    serializer_class = SemillaSerializer

class SemilleroViewSet(viewsets.ModelViewSet):
    queryset = Semillero.objects.all()
    serializer_class = SemilleroSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


#Vista para mostrar semilleros por actividad

#Vista para mostrar semilleros por creador

#Vista muestra semilleros por fecha decreciente - creciente


