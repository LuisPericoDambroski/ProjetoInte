from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Registre todos os models não-abstratos
admin.site.register(Acessorio)
admin.site.register(Armadura)
admin.site.register(Arma)
admin.site.register(ItemGeral)
admin.site.register(Esoterico)
admin.site.register(Alquimico)
admin.site.register(Melhoria)
admin.site.register(Magia)
admin.site.register(Poder)
admin.site.register(Condicao)
admin.site.register(MaterialEspecial)
admin.site.register(Veiculo)
admin.site.register(Armadilha)
admin.site.register(Doenca)