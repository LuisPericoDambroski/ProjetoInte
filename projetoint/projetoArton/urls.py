from django.urls import path
from projetoArton.views import (
    home,
    login_view,
    register_view,
    dashboard,
    logout_view,
    forgot_password,
    reset_password,
)
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path('teste/', views.teste, name="teste"),
    
    # Recuperação de senha
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/<int:uid>/<str:token>/", reset_password, name="reset_password"),
]
