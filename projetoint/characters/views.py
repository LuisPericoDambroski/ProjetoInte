from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Character
from users.models import CustomUser
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

# Lista de personagens
def character_list(request):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    characters = Character.objects.filter(user=user)
    can_create_more = characters.count() < 4
    return render(request, "characters/character_list.html", {
        "characters": characters,
        "can_create_more": can_create_more
    })


# Criar Personagem
def create_character(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)

        # Verifica se o usuário já tem 4 personagens
        if Character.objects.filter(user=user).count() >= 4:
            messages.error(request, "Você atingiu o limite máximo de 4 fichas.")
            return redirect("lista")  # ou redirecione de volta para a página de criação, se preferir

        name = request.POST.get("name")
        character = Character.objects.create(name=name, user=user)
        return redirect("lista")

    return render(request, "characters/create_character.html")

# Detalhes da ficha
def character_detail(request, id):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)
    return render(request, "characters/character_detail.html", {"character": character})


# Atualizar ficha
def update_character(request, id):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)

    if request.method == "POST":
        character.char_class = request.POST.get("char_class")
        character.origin = request.POST.get("origin")
        character.deity = request.POST.get("deity")
        character.race = request.POST.get("race")
        character.level = request.POST.get("level")
        character.image = request.FILES.get("image") or character.image

        # Proteção extra: evita sobrescrever name com None
        if request.POST.get("name"):
            character.name = request.POST.get("name")

        character.save()
        return redirect("lista")

    return render(request, "characters/character_detail.html", {"character": character})


# Confirmação de exclusão
def confirm_delete_character(request, id):
    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)
    return render(request, "characters/delete_character.html", {"character": character})

# Deletar personagem
def delete_character(request, id):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        character = get_object_or_404(Character, id=id, user=user)
        character.delete()
        return redirect("lista")
    return HttpResponseNotAllowed(['POST'])

# Trocar nome
def trocar_nome(request, id):
    print(">>> Entrou na view de troca de nome")  # Debug

    user_id = request.session.get("user_id")
    user = get_object_or_404(CustomUser, id=user_id)
    character = get_object_or_404(Character, id=id, user=user)

    if request.method == "POST":
        novo_nome = request.POST.get("new_name")
        print("Novo nome recebido:", novo_nome)  # Debug

        if character.can_change_name:
            character.name = novo_nome
            character.last_name_change = timezone.now()
            character.save()
            messages.success(request, "Nome alterado com sucesso!")
        else:
            messages.error(request, "Você só pode trocar o nome a cada 1 mês.")

    return redirect("character_detail", id=character.id)
