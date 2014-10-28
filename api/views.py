from api.models import Logro
from rest_framework import viewsets
from api.serializers import LogroSerializer


class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer


#Vista para mostrar semilleros por actividad

#Vista para mostrar semilleros por creador

#Vista muestra semilleros por fecha decreciente - creciente


