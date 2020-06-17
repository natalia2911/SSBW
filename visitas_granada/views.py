    #latest_visita_list = list(Visita.objects.order_by('likes')[:3])
    #template = loader.get_template('visitas_granada/index.html')
    #context = {'visita': latest_visita_list,'test': "test888"}
from django.shortcuts import render, HttpResponse, redirect
from .models import Visita, Comentario, VisitaForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib import messages

from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from .serializers import VisitaSerializer, ComentarioSerializer, LikeSerializer

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

def index(request):
    visitas = Visita.objects.all()
    comentarios = Comentario.objects.all()
    context = {'visitas': visitas, 'comentarios': comentarios}
    return render(request, 'card.html', context)

def detalle(request, name):
    visita = Visita.objects.get(nombre=name)
    comentarios = Comentario.objects.all()
    context = {'visita': visita, 'comentarios': comentarios}
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
    return render(request, "añadir_visita.html", {'form': form})

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
def visita_likes(request, name):
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
