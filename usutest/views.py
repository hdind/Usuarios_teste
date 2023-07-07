from django.shortcuts import render, redirect, HttpResponse
from usutest.forms import LoginAccountForms, CreateAccountForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginAccountForms()

    if request.method == 'POST':
        form = LoginAccountForms(request.POST)

        if form.is_valid():
            nome = form['username'].value()
            senha = form['password'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return HttpResponse('Usuário logado com sucesso!')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usutest/login.html', {'form': form})

def create_account(request):
    form = CreateAccountForms()

    if request.method == 'POST':
        form = CreateAccountForms(request.POST)

        if form.is_valid():
            nome=form['username_create'].value()
            email=form['email'].value()
            senha=form['password_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usutest/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')