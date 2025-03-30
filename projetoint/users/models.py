from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=255)
    reset_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Poder(models.Model):
    TIPO_CHOICES = [
        ('combate', 'Combate'),
        ('destino', 'Destino'),
        ('magia', 'Magia'),
        ('concedido', 'Concedido'),
        ('tormenta', 'Tormenta'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Personagem(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    poderes = models.ManyToManyField(Poder)
    
    def __str__(self):
        return f"Personagem de {self.usuario.username}"

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

#     nome = models.CharField(max_length=50, unique=True)
#     descricao = models.TextField()
#     tipo_escolhas = [
#         (1, 'Tormenta'),
#         (2, 'D&D'),
#         (3, 'Concedido'),
#  ]
#     tipo = models.IntegerField(choices=tipo_escolhas, default=1)
#     concedente = models.ForeignKey(null=True)