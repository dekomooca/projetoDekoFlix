from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import  forms

class FormHomePage(forms.Form): #vai ter um campo apenas, vamos usar o formulario padrao do django
    email = forms.EmailField(label=False)

class CriarContaForm(UserCreationForm):
    # Crio uma subclasse chamada Meta pois é o padrao que o djando pede, e dizemos para ela que
    # O modelo que vamos utilizar como referencia para gerenciar nosso usuario.
    # No caso criamos o Usuario em models, entao vamos replicar a criacao do form padrao do djando,
    # baseado nas informacoes do modelo de Usuario
    email = forms.EmailField()
    class Meta:
        model = Usuario
        #Aqui vamos dizer quais campos vao ser exibidos no formulario. campo email é o que criamos acima
        fields = ('username', 'email', 'password1', 'password2')