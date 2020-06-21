    #latest_visita_list = list(Visita.objects.order_by('likes')[:3])
    #template = loader.get_template('visitas_granada/index.html')
    #context = {'visita': latest_visita_list,'test': "test888"}
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Visita, Comentario, VisitaForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib import messages
from django.core.exceptions import ValidationError
from django import forms

from rest_framework import viewsets, permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .serializers import VisitaSerializer, ComentarioSerializer, LikeSerializer

import requests
import json

import os
import datetime

import logging
logger = logging.getLogger(__name__)

def index(request):
    latest_visita_list = list(Visita.objects.order_by('-likes')[:])
    numero_visitas = Visita.objects.count()
    context = {'visitas': latest_visita_list, 'n_visitas': numero_visitas}
    return render(request, 'card.html', context)

def detalle(request, name):
    visita = Visita.objects.get(nombre=name)
    comentarios = Comentario.objects.all()
    numero_visitas = Visita.objects.count()

    site = visita.nombre.replace(" ", "+") + "+Granada"
    uri = 'https://nominatim.openstreetmap.org/search?q={}&format=json'.format(site)
    result = requests.get(uri)
    data = json.loads(result.text)
    lat = data[0]['lat']
    lon = data[0]['lon']
    print(data)
    print(lat)
    print(lon)

    context = {'visita': visita, 'comentarios': comentarios, 'n_visitas': numero_visitas, 'lat': lat, 'lon': lon}
    return render(request, 'detalle.html', context)


def añadir_visita(request):
    			
    if request.method == 'POST':   # de vuelta con los datos

        form = VisitaForm(request.POST, request.FILES) #  bound the form

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print(form.errors)		
    else:
        form = VisitaForm()
    # GET o error	
    numero_visitas = Visita.objects.count()
    context = {'form': form, 'n_visitas': numero_visitas}
    return render(request, "añadir_visita.html", context)

def editar_visita(request, name):
    visita = Visita.objects.get(nombre=name)
    form = VisitaForm(instance=visita)

    if request.method == 'POST':
        form = VisitaForm(request.POST, request.FILES)

        if form.is_valid():
            visita.nombre = form.cleaned_data["nombre"]
            visita.descripción = form.cleaned_data["descripción"]
            
            if form.cleaned_data["foto"]:
                visita.foto = form.cleaned_data["foto"]
            
            visita.save()
            return redirect(index)
    else:    
        context = {'form': form, 'nombre': name}
        return render(request, "editar_visita.html", context)


def borrar_visita(request, name):
    visita = Visita.objects.get(nombre=name)
    visita.delete()
    return redirect(index)

class VisitaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Visita.objects.all()#.order_by('nombre')
    serializer_class = VisitaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

@csrf_exempt
def api_likes(request, name):
    try:
        visita = Visita.objects.get(nombre=name)
    except Visita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
         serializer = LikeSerializer(visita)
         return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LikeSerializer(visita, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)
