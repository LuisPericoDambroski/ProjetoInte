from django.contrib import admin
from django.urls import path, include  # 🔥 O "include" é necessário para importar as URLs do app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("projetoArton.urls")),  # 🔥 Isso garante que as URLs do app sejam carregadas!
]
