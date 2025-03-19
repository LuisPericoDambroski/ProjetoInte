from django.apps import AppConfig

class usersconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # Nome deve ser exatamente como está no INSTALLED_APPS