from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from usutest.models import FormUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login_account(request):
    form = FormUser()
    return render(request, 'usutest/login.html', {'form': form})

def create_account(self, request):
    form = self.FormUser(request.POST)
    if form.is_valid():
        login_data = form.cleaned_data
        user = authenticate(request, login=login_data["login"], password=login_data["password"])
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirecionar para a página principal após o login
    return render(request, "login.html", {"form": form})

def logout_account(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')