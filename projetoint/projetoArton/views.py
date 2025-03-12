from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home (request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'Login.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else: 
        user = User.objects.create_user(
        username=request.POST['username'], 
        password=request.POST['password'], 
        email=request.POST['email'],)
        
        data['msg'] = 'Usuário cadastrado com sucesso'
        data['class'] = 'alert-sucess'
    return render(request, 'Login.html', data) 