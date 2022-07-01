from django.urls import path
from .views import *



urlpatterns = [   
    path('carga-familiares/', carga_familiares),
    path('familiares/', familiares),
    path('', inicio),
]