from rest_framework.serializers import ModelSerializer
from apps.avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            'usuario',
            'comentario',
            'nota',
            'data',
        )
