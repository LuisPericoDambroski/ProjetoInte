from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import CustomUser
from . import models
import bcrypt
import random
import string
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET


def home(request):
    return render(request, "index.html", {'request': request})

def fichas_personagens(request):
    return render(request, 'Ficha.html')

# def poderes(request):
#     tipo = request.GET.get('tipo', '')  # Obtém o parâmetro tipo da URL
    
#     # Aqui você pode filtrar os poderes com base no tipo
#     context = {
#         'tipo_selecionado': tipo,
#         # Outros dados que você queira passar para o template
#     }
    
#     return render(request, 'poderes.html', context)

def concedidos(request):
    # Aqui você pode adicionar a lógica específica para os poderes concedidos
    context = {
        'titulo': 'Poderes Concedidos',
        # Outros dados específicos para concedidos
    }
    return render(request, 'concedidos.html', context)

def classes (request):
    return render(request, 'classes.html')

def racas (request):
    return render(request, 'racas.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password").encode('utf-8')  # Encode para bytes
        
        try:
            user = CustomUser.objects.get(username=username)
            if bcrypt.checkpw(password, user.password.encode('utf-8')):  # Comparação segura
                request.session['user_id'] = user.id  # 🔥 Salvando ID do usuário na sessão
                request.session['username'] = user.username
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home")  # Redireciona para o painel do usuário
            else:
                messages.error(request, "Usuário ou senha incorretos.")
        except CustomUser.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("/login/?modal=register")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return redirect("/login/?modal=register")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return redirect("/login/?modal=register")

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user = CustomUser(username=username, email=email, password=hashed_password)
        user.save()

        request.session['user_id'] = user.id

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("/login/?modal=register")

    return redirect("/login/")


def dashboard(request):
    if "user_id" not in request.session:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")

    user = CustomUser.objects.get(id=request.session["user_id"])
    return render(request, "dashboard.html", {"user": user})


def logout_view(request):
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect('home')  # Redireciona para a página inicial


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = CustomUser.objects.get(email=email)
            reset_token = "".join(random.choices(string.ascii_letters + string.digits, k=32))
            user.reset_token = reset_token
            user.save()

            reset_link = f"http://127.0.0.1:8000/reset-password/{user.id}/{reset_token}/"
            send_mail(
                "Redefinição de Senha",
                f"Para redefinir sua senha, clique no link: {reset_link}",
                "noreply@seusite.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "E-mail de redefinição enviado!")
        except CustomUser.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")

        return redirect("login")

    return render(request, "forgot_password.html")


def reset_password(request, uid, token):
    try:
        user = CustomUser.objects.get(id=uid, reset_token=token)
    except CustomUser.DoesNotExist:
        messages.error(request, "Token inválido ou expirado.")
        return redirect("login")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect(f"/reset-password/{uid}/{token}/")

        user.password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user.reset_token = None
        user.save()

        messages.success(request, "Senha redefinida com sucesso!")
        return redirect("login")

    return render(request, "reset_password.html", {"uid": uid, "token": token})

# from django.views.decorators.csrf import csrf_exempt
# from .models import Poder, Personagem
# import json

# @require_GET
# def listar_poderes(request):
#     tipo = request.GET.get('tipo')
#     if tipo:
#         poderes = Poder.objects.filter(tipo=tipo).values('nome')
#         return JsonResponse({'poderes': list(poderes)})
#     return JsonResponse({'poderes': []})

# @require_GET
# def obter_descricao_poder(request):
#     nome = request.GET.get('nome')
#     try:
#         poder = Poder.objects.get(nome=nome)
#         return JsonResponse({'descricao': poder.descricao})
#     except Poder.DoesNotExist:
#         return JsonResponse({'descricao': 'Descrição não disponível.'})

# @csrf_exempt
# def salvar_poder(request):
#     if request.method == 'POST' and request.user.is_authenticated:
#         try:
#             data = json.loads(request.body)
#             poder = Poder.objects.get(nome=data['nome'], tipo=data['tipo'])
            
#             # Obtém ou cria o personagem do usuário
#             personagem, created = Personagem.objects.get_or_create(
#                 usuario=request.user
#             )
            
#             # Adiciona o poder ao personagem
#             personagem.poderes.add(poder)
            
#             return JsonResponse({'success': True})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})
#     return JsonResponse({'success': False, 'error': 'Requisição inválida ou usuário não autenticado'})