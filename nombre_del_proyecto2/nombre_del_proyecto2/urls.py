from django.urls import path
from django.contrib import admin
from nombre_de_la_aplicacion.views import obtener_tipodocumento, tipodocumento_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', obtener_tipodocumento, name='tipodocumento'),
    path('api/tipodocumentos/', tipodocumento_list, name='tipodocumento_list'),
]