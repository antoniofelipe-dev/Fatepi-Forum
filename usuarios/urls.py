from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair')
]
