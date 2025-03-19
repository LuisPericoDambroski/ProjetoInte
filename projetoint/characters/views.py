from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Character, CustomUser


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters})


def create_character(request):
    user_id = request.session.get('user_id')  # 🔥 Obtém usuário da sessão

    if not user_id:
        return redirect("login")  # 🔥 Se não estiver logado, redireciona

    user = CustomUser.objects.get(id=user_id)  # Obtém o usuário autenticado

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        Character.objects.create(user=user, name=name, description=description)
        return redirect("characters")  # Ajuste para a URL correta

    return render(request, "characters/create.html")

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'characters/character_detail.html', {'character': character})

def edit_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    
    if request.method == "POST":
        character.name = request.POST.get("name")
        character.description = request.POST.get("description")
        character.save()
        return redirect('character_list')

    return render(request, 'characters/edit_character.html', {'character': character})

def delete_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    
    if request.method == "POST":
        character.delete()
        return redirect('character_list')

    return render(request, 'characters/delete_character.html', {'character': character})
