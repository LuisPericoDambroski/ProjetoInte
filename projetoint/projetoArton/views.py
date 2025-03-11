from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from .forms import RegisterForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redireciona para a página inicial após o login
            else:
                form.add_error(None, "Credenciais inválidas")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário no banco de dados
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
