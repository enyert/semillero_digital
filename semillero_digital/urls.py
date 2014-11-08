from django.conf.urls import patterns, include, url
from rest_framework import routers
from api import views
from login.views import *
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
    url(r'^index/', index),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/crearSemillero/$', crearSemillero),
    url(r'^accounts/buscar/$', basicSearch),
    url(r'^accounts/profile/$', home),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
)
