from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='card'),
    path('detalle/', views.detalle, name='detalle'),
    path('añadir_visita/', views.añadir_visita, name='añadir_visita'),
]
