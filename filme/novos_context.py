#Diferente das variaveis padroes globais do Django como Usuario, Objetc, Lista de objetos
#Aqui nos criamos nossas variaveis globais para serem usadas em todos html
import random

from .models import Filme

def lista_filmes_recentes(request):
    #-data_criacao: order by desc
    #data_criacao: order by asc
    lista_filmes_recentes = Filme.objects.all().order_by('data_criacao')[0:6]
    filme_destaque = random.choice(Filme.objects.all())
    return {"filme_destaque": filme_destaque}
    return {"lista_filmes_recentes": lista_filmes_recentes, "filme_destaque":filme_destaque}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:6]
    return {"lista_filmes_emalta": lista_filmes}

# def filme_destaque(request):
#     # filme = Filme.objects.order_by('visualizacao')[0]
#     filme = random.choice(Filme.objects.all())
#     return {"filme_destaque": filme}
    # filme = Filme.objects.all().order_by('-data_criacao')[0:8]
    # if filme:
    #     filme_destaque = filme
    # else:
    #     filme_destaque = None
    # #filme = random.choice(Filme.objects.all())
    # return {"filme_destaque": filme}