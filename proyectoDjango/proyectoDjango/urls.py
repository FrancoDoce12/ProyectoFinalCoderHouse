"""proyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from django.contrib import admin
from django.urls import path

from proyectoDjango.views import saludo, dia_De_Hoy, nombre_de, template1, en_que_ano_naciste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('hoy/', dia_De_Hoy),
    # como hacer un patch dinamico 
    # el argumento "nombree" que recibe la def "nombre_de" es recibido a traves de lo que se escriba en la url
    path('mi_nombre_es/<nombre>', nombre_de),
    # primer template
    path('template_1/', template1),
    #ejercicio del año en el que naciste
    path('en_que_año_naciste/<edad>/', en_que_ano_naciste),
    
    
]
 