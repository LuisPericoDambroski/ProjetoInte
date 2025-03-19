from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.test.client import Client

client = Client()

# Simulando login
user = User.objects.get(username="gab")  # Substitua pelo nome do usuário real
client.force_login(user)  # 🔥 Força login sem senha

# Testando se o usuário está autenticado na sessão
print("✅ Usuário autenticado:", get_user(client))
