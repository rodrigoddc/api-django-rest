from rest_framework.serializers import ModelSerializer
from apps.enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'logradouro',
            'numero',
            'complemento',
            'cidade',
            'estado',
            'latitude',
            'longitude',
        )
