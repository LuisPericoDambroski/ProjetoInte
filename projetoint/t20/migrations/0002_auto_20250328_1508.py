# Generated by Django 3.0.4 on 2025-03-28 18:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t20', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'Acessório', 'verbose_name_plural': 'Acessórios'},
        ),
        migrations.AlterModelOptions(
            name='alquimico',
            options={'verbose_name': 'Alquímico', 'verbose_name_plural': 'Alquímicos'},
        ),
        migrations.AlterModelOptions(
            name='arma',
            options={'verbose_name': 'Arma', 'verbose_name_plural': 'Armas'},
        ),
        migrations.AlterModelOptions(
            name='armadilha',
            options={'verbose_name': 'Armadilha', 'verbose_name_plural': 'Armadilhas'},
        ),
        migrations.AlterModelOptions(
            name='armadura',
            options={'verbose_name': 'Armadura', 'verbose_name_plural': 'Armaduras'},
        ),
        migrations.AlterModelOptions(
            name='condicao',
            options={'verbose_name': 'Condição', 'verbose_name_plural': 'Condições'},
        ),
        migrations.AlterModelOptions(
            name='doenca',
            options={'verbose_name': 'Doença', 'verbose_name_plural': 'Doenças'},
        ),
        migrations.AlterModelOptions(
            name='esoterico',
            options={'verbose_name': 'Esotérico', 'verbose_name_plural': 'Esotéricos'},
        ),
        migrations.AlterModelOptions(
            name='itemgeral',
            options={'verbose_name': 'Item Geral', 'verbose_name_plural': 'Itens Gerais'},
        ),
        migrations.AlterModelOptions(
            name='magia',
            options={'verbose_name': 'Magia', 'verbose_name_plural': 'Magias'},
        ),
        migrations.AlterModelOptions(
            name='materialespecial',
            options={'verbose_name': 'Material Especial', 'verbose_name_plural': 'Materiais Especiais'},
        ),
        migrations.AlterModelOptions(
            name='melhoria',
            options={'verbose_name': 'Melhoria', 'verbose_name_plural': 'Melhorias'},
        ),
        migrations.AlterModelOptions(
            name='poder',
            options={'verbose_name': 'Poder', 'verbose_name_plural': 'Poderes'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veículo', 'verbose_name_plural': 'Veículos'},
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='tipo',
            field=models.CharField(choices=[('menor', 'Menor'), ('medio', 'Médio'), ('maior', 'Maior')], default='menor', max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='duracao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='efeito',
            field=models.TextField(blank=True, null=True, verbose_name='Efeito'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='nivel',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='alquimico',
            name='tipo',
            field=models.CharField(choices=[('preparado', 'Preparado'), ('catalisador', 'Catalisador'), ('veneno', 'Veneno')], default='preparado', max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='alcance',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Alcance'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='classe',
            field=models.CharField(choices=[('simples', 'Simples'), ('marcial', 'Marcial'), ('exotica', 'Exótica')], default='simples', max_length=20, verbose_name='Classe'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='critico',
            field=models.CharField(max_length=20, verbose_name='Crítico'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='dano',
            field=models.CharField(max_length=20, verbose_name='Dano'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='empunhadura',
            field=models.CharField(choices=[('uma-mao', 'Uma mão'), ('duas-maos', 'Duas mãos'), ('leve', 'Leve')], default='uma-mao', max_length=20, verbose_name='Empunhadura'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='t20.MaterialEspecial', verbose_name='Material Especial'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='melhorias',
            field=models.ManyToManyField(blank=True, to='t20.Melhoria', verbose_name='Melhorias'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='tipo',
            field=models.CharField(choices=[('perfuracao', 'Perfuração'), ('corte', 'Corte'), ('impacto', 'Impacto')], default='corte', max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='cd_resistencia',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='CD de Resistência'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='efeito',
            field=models.TextField(verbose_name='Efeito'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='gatilho',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gatilho'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='magica',
            field=models.BooleanField(default=False, verbose_name='Mágica'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='nivel',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='armadilha',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='bonus_defesa',
            field=models.IntegerField(default=0, verbose_name='Bônus de Defesa'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='classe',
            field=models.CharField(choices=[('leve', 'Leve'), ('pesada', 'Pesada'), ('escudo', 'Escudo')], default='leve', max_length=20, verbose_name='Classe'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='modificadores',
            field=models.TextField(blank=True, null=True, verbose_name='Modificadores'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='penalidade',
            field=models.IntegerField(default=0, verbose_name='Penalidade'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='armadura',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='condicao',
            name='cura',
            field=models.TextField(blank=True, null=True, verbose_name='Cura'),
        ),
        migrations.AlterField(
            model_name='condicao',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='condicao',
            name='efeitos',
            field=models.TextField(verbose_name='Efeitos'),
        ),
        migrations.AlterField(
            model_name='condicao',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='sintomas',
            field=models.TextField(verbose_name='Sintomas'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='tempo_incubacao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tempo de Incubação'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='tratamento',
            field=models.TextField(blank=True, null=True, verbose_name='Tratamento'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='nivel',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='requisitos',
            field=models.TextField(blank=True, null=True, verbose_name='Requisitos'),
        ),
        migrations.AlterField(
            model_name='esoterico',
            name='tipo',
            field=models.CharField(choices=[('encantamento', 'Encantamento'), ('pocao', 'Poção'), ('material', 'Material Especial')], default='encantamento', max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='categoria',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='itemgeral',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='acao',
            field=models.CharField(max_length=50, verbose_name='Ação'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='alcance',
            field=models.CharField(max_length=50, verbose_name='Alcance'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='alvo',
            field=models.CharField(max_length=100, verbose_name='Alvo'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='aprimoramentos',
            field=models.TextField(blank=True, null=True, verbose_name='Aprimoramentos'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='ciclo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Ciclo'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='classe',
            field=models.CharField(choices=[('arcana', 'Arcana'), ('divina', 'Divina'), ('universal', 'Universal')], max_length=20, verbose_name='Classe'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='duracao',
            field=models.CharField(max_length=50, verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='escola',
            field=models.CharField(choices=[('abjuracao', 'Abjuração'), ('adivinhacao', 'Adivinhação'), ('convocacao', 'Convocação'), ('encantamento', 'Encantamento'), ('evocacao', 'Evocação'), ('ilusao', 'Ilusão'), ('necromancia', 'Necromancia'), ('transmutacao', 'Transmutação')], max_length=20, verbose_name='Escola'),
        ),
        migrations.AlterField(
            model_name='magia',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='custo',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Custo'),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='modificador',
            field=models.CharField(max_length=50, verbose_name='Modificador'),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='materialespecial',
            name='tipo_item',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tipo de Item'),
        ),
        migrations.AlterField(
            model_name='melhoria',
            name='custo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Custo'),
        ),
        migrations.AlterField(
            model_name='melhoria',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='melhoria',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='melhoria',
            name='requisitos',
            field=models.TextField(blank=True, null=True, verbose_name='Requisitos'),
        ),
        migrations.AlterField(
            model_name='melhoria',
            name='tipo',
            field=models.CharField(choices=[('arma', 'Arma'), ('armadura', 'Armadura'), ('escudo', 'Escudo'), ('esoterico', 'Esotérico'), ('ferramenta', 'Ferramenta'), ('vestuario', 'Vestuário'), ('qualquer', 'Qualquer')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='poder',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='poder',
            name='deuses',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Deuses'),
        ),
        migrations.AlterField(
            model_name='poder',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='poder',
            name='requisitos',
            field=models.TextField(blank=True, null=True, verbose_name='Requisitos'),
        ),
        migrations.AlterField(
            model_name='poder',
            name='tipo',
            field=models.CharField(choices=[('combate', 'Combate'), ('destino', 'Destino'), ('magia', 'Magia'), ('concedido', 'Concedido')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='capacidade',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='origem',
            field=models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton')], default='T20', max_length=20, verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='tipo',
            field=models.CharField(choices=[('terrestre', 'Terrestre'), ('aquatico', 'Aquático'), ('aereo', 'Aéreo')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='tripulacao',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tripulação'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='velocidade',
            field=models.CharField(max_length=50, verbose_name='Velocidade'),
        ),
    ]
