from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from apps.avaliacoes.api.serializers import AvaliacaoSerializer
from apps.avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['data', 'usuario__username', 'comentario']
    lookup_field = 'id'
