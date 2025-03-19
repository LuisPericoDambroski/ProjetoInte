from django.db import models
from users.models import CustomUser  # Importa o usuário customizado

class Character(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 🔥 Relaciona ao usuário customizado
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
