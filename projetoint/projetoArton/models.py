from django.db import models

class Acessorio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    preco = models.IntegerField()
    descricao = models.TextField()