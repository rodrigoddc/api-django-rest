from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=150, null=True, blank=True)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.logradouro

