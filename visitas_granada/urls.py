from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='card'),
    path('detalle/<str:name>', views.detalle, name='detalle'),
    path('añadir_visita/', views.añadir_visita, name='añadir_visita'),
    path('editar_visita/<str:name>', views.editar_visita, name='editar_visita'),
    path('borrar_visita/<str:name>', views.borrar_visita, name='borrar_visita'),
    path('likes/<str:name>', views.visita_likes, name='likes'),
]
