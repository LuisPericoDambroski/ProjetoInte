from django.core.validators import EmailValidator
from django.db import models

class CustomUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=255)
    reset_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

