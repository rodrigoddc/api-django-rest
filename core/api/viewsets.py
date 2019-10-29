from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    # sobrescreve o querset do ModelViewSet
    def get_queryset(self):
        return PontoTuristico.objects.all()
        # return PontoTuristico.objects.filter(aprovado=True)

    # Sobrescreve o método GET do ModelViewSet para retorno de LISTA DE OBJETOS
    # def list(self, request, *args, **kwargs):
    #     return Response(
    #         {
    #             'teste': 123
    #         }
    #     )

    # Sobrescreve o método POST do ModelViewSet para instanciar objeto
    def create(self, request, *args, **kwargs):
        return Response(
            {
                'Hello': request.data['nome']
            }
        )

    # Sobrescreve o método GET do ModelViewSet
    def destroy(self, request, *args, **kwargs):
        pass

    # Sobrescreve o método GET do ModelViewSet para retorno de UM ÚNICO DE OBJETOS
    def retrieve(self, request, *args, **kwargs):
        pass

    # Sobrescreve o método PUT do ModelViewSet para ATUALIZAÇÃO COMPLETA de OBJETO
    def update(self, request, *args, **kwargs):
        pass

    # Sobrescreve o método PATCH do ModelViewSet para ATUALIZAÇÃO PARCIAL OBJETO
    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['POST', 'GET'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['GET'], detail=False)
    def teste(self, request):
        pass

