from django.urls import path
from usutest.views import login_account, create_account, logout_account

urlpatterns = [
    path('login', login_account, name='login'),
    path('cadastro', create_account, name='cadastro'),
    path('logout', logout_account, name='logout'),
]