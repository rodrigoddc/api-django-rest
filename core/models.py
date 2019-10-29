from django.db import models
from apps.atracoes.models import Atracao
from apps.comentarios.models import Comentario
from apps.avaliacoes.models import Avaliacao
from apps.enderecos.models import Endereco


class PontoTuristico(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, blank=True)
    comentarios = models.ManyToManyField(Comentario, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
