from django.conf.urls import patterns, include, url
from rest_framework import routers
from api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register('logros', views.LogroViewSet)
router.register('semillas', views.SemillaViewSet)
router.register('semilleros', views.SemilleroViewSet)
router.register('actividades', views.ActividadViewSet)
router.register('eventos', views.EventoViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
