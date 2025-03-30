from django.urls import path
from .views import login_view, home, register_view, dashboard, logout_view, forgot_password, reset_password, fichas_personagens, classes, racas, concedidos

urlpatterns = [
    path("", home, name="home"),
    path("ficha/", fichas_personagens, name = "ficha"),
    path("login/", login_view, name="login"),  # 🔥 Garante que a URL existe com o nome correto
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("classe/", classes, name="classes" ),
    path("raças/", racas, name="racas" ),
    # path("poderes/", poderes, name="poderes"),
    path("poderes/concedidos/", concedidos, name="concedidos"),
    # path('teste/', views.teste, name="teste"),

    # # path('api/poderes/', listar_poderes, name='listar_poderes'),
    # path('api/poderes/descricao/', obter_descricao_poder, name='obter_descricao_poder'),
    # path('api/poderes/salvar/', salvar_poder, name='salvar_poder'),
    
    # Recuperação de senha
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/<int:uid>/<str:token>/", reset_password, name="reset_password"),
]
