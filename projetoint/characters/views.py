from users.utils import get_real_user
from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from users.models import CustomUser
from django.http import HttpResponseNotAllowed
from datetime import timedelta
from django.utils import timezone
from users.utils import get_real_user  # ajuste o import se necessário





# Lista de personagens
def character_list(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect('login')  # ou outra lógica de acesso

    user = get_object_or_404(CustomUser, id=user_id)
    characters = Character.objects.filter(user=user)
    return render(request, "characters/character_list.html", {"characters": characters})


# Criação simples com apenas o nome
def create_character(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if request.user.is_authenticated:
            user = request.user.user  # 👈 acessa o CustomUser real
            character = Character.objects.create(name=name, user=user)
            return redirect("lista")  # ajuste conforme sua URL
        else:
            return redirect("login")

    return render(request, "characters/novo.html")




# Página de detalhes e edição da ficha
def character_detail(request, id):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)

    if request.method == "POST":

        if 'name' in request.POST:
            if not character.last_name_change or timezone.now() - character.last_name_change >= timedelta(days=90):
                character.name = request.POST.get('name')
                character.last_name_change = timezone.now()


        if not character.char_class:
            character.char_class = request.POST.get('classe')

        character.char_class = request.POST.get('classe', character.char_class)


        character.char_class = request.POST.get('classe')
        character.origin = request.POST.get('origem')
        character.deity = request.POST.get('deus')
        character.race = request.POST.get('raca')
        character.skills = request.POST.get('atributos')
        character.powers = request.POST.get('poderes')
        character.inventory = request.POST.get('inventario')


        # Imagem (se estiver sendo usada via upload ou caminho)
        image_path = request.POST.get("image_path")
        if image_path:
            character.image_path = image_path

        if request.FILES.get('image'):
            character.image = request.FILES['image']

            if not character.name:
                character.name = request.POST.get("name", character.name)

        character.save()
        return redirect("lista")

    return render(request, "characters/character_detail.html", {"character": character})



def confirm_delete_character(request, id):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)
    return render(request, "characters/delete_character.html", {"character": character})


def delete_character(request, id):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        character = get_object_or_404(Character, id=id, user=user)
        character.delete()
        return redirect("lista")
    return HttpResponseNotAllowed(['POST'])
