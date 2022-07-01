from django import http
from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

def inicio(request):
    return render (request, "Appcoder/inicio.html")


def carga_familiares(request):
    familiar = Familiar(nombre="Juan Pepe", altura=1.75, fecha_nacimiento="2021-02-03")
    familiar.save()
    familiar = Familiar(nombre="Ariel Camino", altura=1.78, fecha_nacimiento="2016-02-03")
    familiar.save()
    familiar = Familiar(nombre="Brian Oxrud", altura=1.78, fecha_nacimiento="2018-02-03")
    familiar.save()
    texto= f"Familiar creado: {familiar.nombre} {familiar.fecha_nacimiento}"
    return HttpResponse(texto)
   
    
def familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'AppCoder/familiares.html', context={'familiares': familiares})

