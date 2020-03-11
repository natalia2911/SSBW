    #latest_visita_list = list(Visita.objects.order_by('likes')[:3])
    #template = loader.get_template('visitas_granada/index.html')
    #context = {'visita': latest_visita_list,'test': "test888"}
from django.shortcuts import render
from .models import Visita, Comentario

def index(request):
    visitas = Visita.objects.all()
    comentarios = Comentario.objects.all()
    context = {'visitas': visitas, 'comentarios': comentarios}
    #context = {'visitas': visitas, 'total': str(len(visitas))}
    return render(request, 'base.html', context)

