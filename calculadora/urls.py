from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'), #esto sirve para importar la clase vista que esta en el directorio tarea1
    path('procesamiento', views.procesamiento, name='procesamiento'),
]