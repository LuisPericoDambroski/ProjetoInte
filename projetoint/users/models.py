from django.core.validators import EmailValidator
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=255)
    reset_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    


class Acessorio(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    preco = models.IntegerField()
    descricao = models.TextField()
    


# class Alquimico(models.Model):
#     id = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=50, unique=True)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     espacos = models.DecimalField(max_digits=10, decimal_places=2)
#     descricao = models.TextField()
#     tipo_escolhas = [
#         (1, 'Catalisadores'),
#         (2, 'Preparados'),
#         (3, 'Venenos'),
#     ]
#     tipo = models.IntegerField(choices=tipo_escolhas, default=1)

# class Poderes(models.Model):
#     id = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=50, unique=True)
#     descricao = models.TextField()
#     tipo_escolhas = [
#         (1, 'Tormenta'),
#         (2, 'D&D'),
#         (3, 'Concedido'),
#  ]
#     tipo = models.IntegerField(choices=tipo_escolhas, default=1)
#     concedente = models.ForeignKey(null=True)