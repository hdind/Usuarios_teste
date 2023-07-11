from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return HttpResponse('Usuário cadastrado com sucesso.')

def logout(request):
    return HttpResponse('Usuário saiu com sucesso.')
