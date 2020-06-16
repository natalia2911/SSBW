    #latest_visita_list = list(Visita.objects.order_by('likes')[:3])
    #template = loader.get_template('visitas_granada/index.html')
    #context = {'visita': latest_visita_list,'test': "test888"}
from django.shortcuts import render, HttpResponse, redirect
from .models import Visita, Comentario, VisitaForm
from django.contrib.auth import authenticate, login, logout



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

def editar_visita(request, id):
    visita = Visita.objects.get(pk=id)
    form = VisitaForm(instance=visita)

