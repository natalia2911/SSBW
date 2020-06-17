from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='card'),
    path('detalle/$', views.detalle, name='detalle'),
    path('añadir_visita/', views.añadir_visita, name='añadir_visita'),
    path('borrar_visita/<str:nombre_visita>', views.borrar_visita, name='borrar_visita'),
    path('editar_visita/<str:nombre_visita>', views.editar_visita, name='editar_visita'),
]
