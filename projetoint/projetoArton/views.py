from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")  # Certifique-se de que o nome do seu HTML está correto!