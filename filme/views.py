from django.shortcuts import render, redirect
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CriarContaForm, FormHomePage

# Create your views here.

#CLASS BASED VIEW
    #Melhor para listar os itens da sua classe - Orientada a objetos

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario esta autenticado:
            return redirect('filme:homefilmes') #redireciona para o homefilmes
        else:
            return super().get(request, *args, **kwargs)  #redireciona para homepage - A funcao get por default, retornar para url padrao definiada no template, no caso, homepage.html

    def get_success_url(self):
        email = self.request.POST.get("email")
        print(self.request.POST)
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    # Faz tudo que escrevermos no FBV comentado abaixo, mas retorna como object_list
    model = Filme

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    # Sao detalhes compartilhados de um item. object - 1 item do modelo
    model = Filme

    #Antes de rodar o processo, ele é chamado, e nao no final como a funcao abaixo get_context_data
    def get(self, request, *args, **kwargs):
        #descobrir qual filme ele ta acessando
        filme = self.get_object()
        #somar 1 nas visualizacoes daquele filme
        filme.visualizacoes +=1
        #salvar
        filme.save()
        #contabilizar o filme visto pelo user
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(Detalhesfilme, self).get(request, *args, **kwargs)
    #return, redireciona o usuario para a url final

# A funcao do get_context_data é retornar como resposta a variavel context com os valores do dicionario passado
#Dessa forma ele é utilizado somente no final da chamada.
#Essa funcao ja esxite no DetailView root, porem estamos sobreescrevendo
#Essa funcao ficou atrelada apenas a DetalhesFilme, precisamos declarar uma global
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        #[0:5] aqui estamos limitando a pegar ate 5 filmes relacionados
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


########################################################################
#FUNCTION BASED VIEW
    #Funcoes rapidas como se fossem metodos, voltar, abrir, etc
#def homepage(request):
    #return render(request, "homepage.html")

#url - view - template
#O context é onde passa os parametros do model para o html
#def homefilmes(request):
    #context = {}
    # lista_filmes = Filme.objects.all()
    # context["lista_filmes"] = lista_filmes
    # return render(request, "homefilmes.html", context)


class PesquisaFilmes(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    # Sao detalhes compartilhados de um item. object - 1 item do modelo
    model = Filme

    #Funcao para fazer a pesquisa nativa do python. Aqui pego com get, a funcao do 'name'
    #que criei no navbar, na parte do form de pesquisa. O nome query é definido por la, se alterar, mudo aqui
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            #object_list é o nome padrao de uma ListView
            #filtro tudo que contains o termo de pesquisa digitado
            object_list = Filme.objects.filter(titulo__icontains = termo_pesquisa)
            #é possivel fazer desta forma abaixo tambem, somente chamadno do self.model, se mudo o nome da classe em model, ele é alterado
            #object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            object_list = Filme.objects.all()
            return object_list
        #return None = caso nao queria retornar nada

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

class EditaPerfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    #Quais sao os campos que o usuario podera alterar
    #UpdateView automaticamente cria esses campos que serao editados para altera-los
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class CriaConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    #Verifica se tds campos foram validados com sucesso, ai salvamos no banco de dados
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    #smp que FormView for chamado, temos que dizer o que fazer com o sucesso
    def get_success_url(self):
        #essa funcao pede como retorno uma url, dessa forma, ao inves de usar redirect, usamos o reverse
        return reverse('filme:login')
