from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.character_list, name="lista"),
    path("novo/", views.create_character, name="novo"),
    # path("ficha/<int:id>/", views.character_detail, name="character_detail"),
    path("ficha/<int:id>/atualizar/", views.update_character, name="update_character"),
    path("ficha/<int:id>/confirm_delete/", views.confirm_delete_character, name="confirm_delete_character"),
    path("ficha/<int:id>/delete/", views.delete_character, name="delete"),
    path("ficha/<int:id>/trocar_nome/", views.trocar_nome, name="trocar_nome"),
    path("fichas/<int:id>/", views.fichas_personagens, name="fichas" )
]
