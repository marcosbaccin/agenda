from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def local(request, titulo_evento):
    return HttpResponse(Evento.objects.get(titulo=titulo_evento).local)
