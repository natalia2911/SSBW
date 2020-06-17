    #latest_visita_list = list(Visita.objects.order_by('likes')[:3])
    #template = loader.get_template('visitas_granada/index.html')
    #context = {'visita': latest_visita_list,'test': "test888"}
from django.shortcuts import render
from .models import Visita, Comentario
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Visita
from .models import Comentario
from .models import VisitaForm

from django import forms


def index(request):
    visitas = Visita.objects.all()
    comentarios = Comentario.objects.all()
    context = {'visitas': visitas, 'comentarios': comentarios}
    return render(request, 'card.html', context)

def detalle(request):
    visitas = Visita.objects.all()
    comentarios = Comentario.objects.all()
    context = {'visitas': visitas, 'comentarios': comentarios}
    return render(request, 'detalle.html', context)

def añadir_visita(request):
    form = VisitaForm()
			
    if request.method == 'POST':   # de vuelta con los datos

        form = VisitaForm(request.POST, request.FILES) #  bound the form

        if form.is_valid():
            form.save()
            return redirect('index')
			
        context = {
            'form': form
        }
    # GET o error	
    return render(request, "añadir_visita.html", context)

def editar_visita(request, nombre_visita): # nombre_visita cambiar por id
    visita = Visita.objects.get(nombre=nombre_visita)
    form = VisitaForm(instance=visita)

    if request.method == 'POST':
        form = VisitaForm(request.POST, request.FILES)

        if form.is_valid():
            visita.nombre = form.cleaned_data["nombre"]
            visita.descripcion = form.cleaned_data["descripcion"]

            if form.cleaned_data["foto"]:
                visita.foto = form.cleaned_data["foto"]

            visita.save()
            messages.success(request, 'Visita editada con éxito')
            return redirect('index')


    context = {'form': form, 'nombre_visita': nombre_visita}
    return render(request, "visitas_granada/editar_visita.html", context)

def borrar_visita(request, nombre_visita):
    visita = Visita.objects.get(nombre=nombre_visita)
    visita.delete()
    messages.error(request, 'Visita eliminada con éxito')
    return redirect('index')


