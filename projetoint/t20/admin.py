# t20/admin.py
from django.contrib import admin
from .models import (  # Importe todos os modelos necessários
    Acessorio,
    Armadura,
    Arma,
    ItemGeral,
    Esoterico,
    Alquimico,
    Melhoria,
    Magia,
    Poder,
    Condicao,
    MaterialEspecial,
    Veiculo,
    Armadilha,
    Doenca
)

# Registre todos os modelos
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
admin.register(Poder)
class PoderAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'custo_pm')
    list_filter = ('tipo', 'magia')
    filter_horizontal = ('requisito_pericias', 'requisito_poderes')
    readonly_fields = ('get_requisitos_texto',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'tipo', 'descricao')
        }),
        ('Ação e Custo', {
            'fields': ('acao', 'custo_pm', 'magia')
        }),
        ('Requisitos', {
            'fields': (
                'requisito_forca', 'requisito_destreza', 'requisito_constituicao',
                'requisito_inteligencia', 'requisito_sabedoria', 'requisito_carisma',
                'requisito_nivel', 'requisito_pericias', 'requisito_poderes', 'requisito_outros',
                'get_requisitos_texto'
            )
        }),
        ('Aprimoramentos', {
            'fields': ('aprimoramentos',),
            'classes': ('collapse',)
        }),
    )