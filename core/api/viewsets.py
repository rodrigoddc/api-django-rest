from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = PontoTuristicoSerializer

    # sobrescreve o querset do ModelViewSet
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)

        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset

    # Sobrescreve o método GET do ModelViewSet para retorno de LISTA DE OBJETOS
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Sobrescreve o método POST do ModelViewSet para instanciar objeto
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Sobrescreve o método GET do ModelViewSet
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # Sobrescreve o método GET do ModelViewSet para retorno de UM ÚNICO DE OBJETOS
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # Sobrescreve o método PUT do ModelViewSet para ATUALIZAÇÃO COMPLETA de OBJETO
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # Sobrescreve o método PATCH do ModelViewSet para ATUALIZAÇÃO PARCIAL OBJETO
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['POST', 'GET'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['GET'], detail=False)
    def teste(self, request):
        pass

