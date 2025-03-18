from django.urls import path
from .views import login_view, home, register_view, dashboard, logout_view, forgot_password, reset_password

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),  # 🔥 Garante que a URL existe com o nome correto
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    # path('teste/', views.teste, name="teste"),
    
    # Recuperação de senha
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/<int:uid>/<str:token>/", reset_password, name="reset_password"),
]
