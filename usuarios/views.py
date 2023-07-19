from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as logout_django, login as login_django
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def game(request):
    return render(request, 'game.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('game')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'register.html', {'erro': 'Já existe um usuário com esse username'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')

def logout(request):
    logout_django(request)
    return redirect('login')
