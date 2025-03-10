from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Adicione campos personalizados, se necessário
    bio = models.TextField(blank=True, null=True)