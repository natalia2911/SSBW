from rest_framework import serializers

from .models import Visita, Comentario

class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('nombre', 'descripción', 'likes', 'foto')


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('visita', 'texto')


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('likes')
