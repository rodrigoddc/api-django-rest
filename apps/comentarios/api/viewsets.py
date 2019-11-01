from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from apps.comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['aprovado']
