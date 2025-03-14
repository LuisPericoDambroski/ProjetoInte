from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, "Index.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já cadastrado.")
            return redirect("register")

        user = CustomUser(username=username, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("login")  # Redireciona para a página de login após cadastro

    return render(request, "login.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home")  # Redireciona para a página inicial após login
            else:
                messages.error(request, "Senha incorreta.")
                return redirect("login")
        except CustomUser.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return redirect("login")

    return render(request, "login.html")




