#Diferente das variaveis padroes globais do Django como Usuario, Objetc, Lista de objetos
#Aqui nos criamos nossas variaveis globais para serem usadas em todos html
import random

from .models import Filme

def lista_filmes_recentes(request):
    #-data_criacao: order by desc
    #data_criacao: order by asc
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:6]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:6]
    return {"lista_filmes_emalta": lista_filmes}

def filme_destaque(request):
    # filme = Filme.objects.order_by('visualizacao')[0]
    filme = None
    if filme:
        filme = random.choice(Filme.objects.all())
        return {"filme_destaque": filme}
    else:
        return None