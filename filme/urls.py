# Url - View - Template

from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, reverse_lazy
#from filme.views import homepage, homefilmes #FBV
from filme.views import Homepage, Homefilmes, Detalhesfilme, PesquisaFilmes, EditaPerfil, CriaConta  # CBV
from django.contrib.auth import views as auth_view, views
from . import views


#faz a inclusao de todas as urls name para que a url do app principal se comunique
app_name = 'filme'

def logout_view(request):
    logout(request)

#A funcao do name é fazer o redirect para essas urls. O nome deve ser usado exatamente igual p/ funcionar
urlpatterns = [
    #path('', homepage), #FBV
    #path('filmes/', homefilmes), #FBV
    path('', Homepage.as_view(), name='homepage'), #CBV
    path('filmes/', Homefilmes.as_view(), name='homefilmes'), #CBV
    path('filmes/detalhesfilme/<int:id>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilmes.as_view(), name='pesquisafilmes'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editarperfil/<int:pk>', EditaPerfil.as_view(), name='editarperfil'), #CBV
    path('criarconta/', CriaConta.as_view(), name='criarconta'), #CBV
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'), #CBV
]

