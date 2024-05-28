from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
LISTA_CATEGORIAS = (
    #(armazenar_no_db, aparece_para_usuario)
    ("FICCAO_CIENTIFICA", "Ficção Científica"),
    ("FANTASIA", "Fantasia"),
    ("AVENTURA", "Aventura"),
    ("THRILLER", "Thriller"),
    ("OUTROS", "Outros"),
)

# criar filmes
# Para vincular e o Filme aparecer no adm precisamos importa-lo no admin.py
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    #Define o formato do print da String dessa classe, por default é object
    def __str__(self):
        return self.titulo

# criar os episodios
class Episodio(models.Model):
    # Passamos o nome da tabela dentro do ForeignKey para fazer o relacionamento
    # ManytoMany em outros casos
    # related_name é o relacionamento com o Filme, ou seja, episodios sao relacionados agora
    # on_delete = deleta em cascada, se removermos os filmes, remove os episodios tbm
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

#Define o formato do print da String dessa classe, por default é object
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

# criar o usuario
class Usuario(AbstractUser):
    #Muitos users vendo 1 filme, e varios filmes vistos por apenas 1 user - ManyToManyField + Classe que se relaciona
    filmes_vistos = models.ManyToManyField("Filme")