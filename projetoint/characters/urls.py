from django.urls import path
from .views import character_list, create_character, character_detail, edit_character, delete_character

urlpatterns = [
    path('', character_list, name='character_list'),
    path("create/", create_character, name="create_character"),
    path('<int:character_id>/', character_detail, name='character_detail'),
    path('<int:character_id>/edit/', edit_character, name='edit_character'),
    path('<int:character_id>/delete/', delete_character, name='delete_character'),
]
