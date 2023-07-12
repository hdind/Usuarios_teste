from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as logout_django, login as login_django
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login/')
def snakegame(request):
    return render(request, 'snakegame.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return snakegame(request)
        else:
            # TODO HttpResponse('Email ou senha inválidos')
            return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            # TODO HttpResponse('Já existe um usuário com esse username.')
            return render(request, 'login.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return HttpResponse('Usuário cadastrado com sucesso.')

def logout(request):
    logout_django(request)
    return HttpResponse('Usuário saiu com sucesso.')
