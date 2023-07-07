from django.urls import path
from usutest.views import login, create_account, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', create_account, name='cadastro'),
    path('logout', logout, name='logout'),
]