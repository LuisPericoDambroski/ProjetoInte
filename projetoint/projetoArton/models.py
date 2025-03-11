from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    # Definindo um nome de relacionamento exclusivo para evitar conflitos
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Nome exclusivo para CustomUser
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # Nome exclusivo para CustomUser
        blank=True,
    )
