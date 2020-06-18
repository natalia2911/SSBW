from django.urls import path, include
from django.views.generic.base import TemplateView

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views

router = routers.DefaultRouter()
router.register(r'visitas', views.VisitaViewSet)
router.register(r'comentarios', views.ComentarioViewSet)

urlpatterns = [
    path('', views.index, name='card'),
    path('detalle/<str:name>', views.detalle, name='detalle'),
    path('añadir_visita/', views.añadir_visita, name='añadir_visita'),
    path('editar_visita/<str:name>', views.editar_visita, name='editar_visita'),
    path('borrar_visita/<str:name>', views.borrar_visita, name='borrar_visita'),
    path('api/likes/<str:name>', views.api_likes, name='likes'),
    path('api/', include(router.urls)),
]
