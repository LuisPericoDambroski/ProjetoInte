from django.urls import path
from .views import login_view, home, register_view, dashboard, logout_view, forgot_password, reset_password, classes, racas, concedidos, poderes, destino, tormenta, magico, combate, deuses, origens, atributos, armas, magias, regras, itens

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),  # 🔥 Garante que a URL existe com o nome correto
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("classe/", classes, name="classes" ),
    path("raças/", racas, name="racas" ),
    path("poderes/", poderes, name="poderes"),
    path("poderes/destino/", destino, name="destino"),
    path("poderes/tormenta/", tormenta, name="tormenta"),
    path("poderes/magico/", magico, name="magico"),
    path("poderes/combate/", combate, name="combate"),
    path("poderes/concedidos/", concedidos, name="concedidos"),
    path("deuses/", deuses, name="deuses"),
    path("origens/", origens, name="origens"),
    path("atributos/", atributos, name="atributos"),
    path("armas/", armas, name="armas"),
    path("magias/", magias, name="magias"),
    path("regras/", regras, name="regras"),
    path("itens/", itens, name="itens"),

    # path('teste/', views.teste, name="teste"),

    # # path('api/poderes/', listar_poderes, name='listar_poderes'),
    # path('api/poderes/descricao/', obter_descricao_poder, name='obter_descricao_poder'),
    # path('api/poderes/salvar/', salvar_poder, name='salvar_poder'),
    
    # Recuperação de senha
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/<int:uid>/<str:token>/", reset_password, name="reset_password"),
]
