from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario

### Criando novo campo dentro de localhost/admin
#filmes_vistos foi criado dentro de models - class Usuario(AbstractUser)

#exemplo do que ja temos hoje no administrativo:
# ("Informações pessoais", {'fields': ('Primeiro nome', 'Último nome',)})

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)