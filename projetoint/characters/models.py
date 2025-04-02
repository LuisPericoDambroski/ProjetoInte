from django.db import models
from users.models import CustomUser
from django.utils import timezone
from datetime import timedelta

class Character(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    char_class = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    deity = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    image = models.ImageField(upload_to='character_images/', blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    powers = models.TextField(blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)

    last_name_change = models.DateTimeField(null=True, blank=True)

    @property
    def can_change_name(self):
        if self.last_name_change is None:
            return True
        return timezone.now() - self.last_name_change >= timedelta(days=30)


    @property
    def days_until_name_change(self):
        if self.last_name_change is None:
            return 0
        remaining = timedelta(days=30) - (timezone.now() - self.last_name_change)
        return max(0, remaining.days)
