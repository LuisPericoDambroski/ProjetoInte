# Generated by Django 5.1.7 on 2025-03-30 03:31

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('modificadores', models.JSONField(blank=True, default=dict)),
                ('tipo', models.CharField(choices=[('menor', 'Menor'), ('medio', 'Médio'), ('maior', 'Maior'), ('unico', 'Único')], default='medio', max_length=20)),
                ('slots', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3)])),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.DecimalField(decimal_places=1, max_digits=3)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Alquimico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('modificadores', models.JSONField(blank=True, default=dict)),
                ('tipo', models.CharField(choices=[('preparado', 'Preparado'), ('catalisador', 'Catalisador'), ('veneno', 'Veneno'), ('oleo', 'Óleo'), ('extrato', 'Extrato'), ('essencia', 'Essência')], max_length=20)),
                ('nivel', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('ingredientes', models.TextField(blank=True, null=True)),
                ('tempo_preparo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlquimicoCatalisador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.DecimalField(decimal_places=1, max_digits=3)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField(default=0)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Aparencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Armadilha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('efeito', models.TextField()),
                ('resistencia', models.CharField(max_length=100)),
                ('investigacao', models.CharField(max_length=100)),
                ('magica', models.BooleanField()),
                ('nivel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Armadura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('classe', models.CharField(choices=[('leve', 'Leve'), ('pesada', 'Pesada'), ('escudo', 'Escudo'), ('roupa', 'Vestuário')], max_length=20)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.CharField(max_length=10)),
                ('penalidade', models.IntegerField()),
                ('espacos', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArmaduraRandom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('chances', models.IntegerField(default=0)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ArmaRandom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('chances', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('quantidade', models.PositiveSmallIntegerField(blank=True, help_text='Quantidade para itens como flechas, balas, etc.', null=True)),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Condicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('detalhes', models.JSONField()),
            ],
            options={
                'verbose_name': 'Condição',
            },
        ),
        migrations.CreateModel(
            name='CustoMagia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circulo', models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('custo', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('sintomas', models.TextField()),
                ('tratamento', models.TextField(blank=True, null=True)),
                ('tempo_incubacao', models.CharField(blank=True, max_length=50, null=True)),
                ('cd', models.PositiveSmallIntegerField(verbose_name='CD de Resistência')),
            ],
        ),
        migrations.CreateModel(
            name='Encantamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('arma', 'Arma'), ('armadura', 'Armadura'), ('acessorio', 'Acessório')], max_length=20)),
                ('nivel', models.PositiveSmallIntegerField()),
                ('efeito', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='EncantoArma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EncantoArmadura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ErroCritico',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Erro Crítico',
            },
        ),
        migrations.CreateModel(
            name='Esoterico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('modificadores', models.JSONField(blank=True, default=dict)),
                ('tipo', models.CharField(choices=[('encantamento', 'Encantamento'), ('pocao', 'Poção'), ('material', 'Material'), ('pergaminho', 'Pergaminho'), ('runico', 'Rúnico'), ('reliquia', 'Relíquia')], max_length=20)),
                ('nivel', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('requisitos', models.TextField(blank=True, null=True)),
                ('duracao', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EsotericoRandom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('chances', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstatisticaCriaturaEspecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nd', models.CharField(max_length=10)),
                ('ataque', models.CharField(max_length=10)),
                ('dano', models.CharField(max_length=10)),
                ('defesa', models.CharField(max_length=10)),
                ('res_forte_80', models.CharField(max_length=10, verbose_name='Resistência Forte (80%)')),
                ('res_media_50', models.CharField(max_length=10, verbose_name='Resistência Média (50%)')),
                ('res_fraca_20', models.CharField(max_length=10, verbose_name='Resistência Fraca (20%)')),
                ('pv', models.IntegerField(verbose_name='Pontos de Vida')),
                ('CD', models.IntegerField(verbose_name='Classe de Dificuldade')),
                ('tipo', models.CharField(choices=[('combate', 'Combate'), ('magico', 'Mágico'), ('suporte', 'Suporte'), ('chefe', 'Chefe')], default='combate', help_text='Tipo especial da criatura', max_length=20)),
            ],
            options={
                'verbose_name': 'Estatística de Criatura Especial',
                'verbose_name_plural': 'Estatísticas de Criaturas Especiais',
                'ordering': ['nd'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EstatisticaCriaturaLacaio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nd', models.CharField(max_length=10)),
                ('ataque', models.CharField(max_length=10)),
                ('dano', models.CharField(max_length=10)),
                ('defesa', models.CharField(max_length=10)),
                ('res_forte_80', models.CharField(max_length=10, verbose_name='Resistência Forte (80%)')),
                ('res_media_50', models.CharField(max_length=10, verbose_name='Resistência Média (50%)')),
                ('res_fraca_20', models.CharField(max_length=10, verbose_name='Resistência Fraca (20%)')),
                ('pv', models.IntegerField(verbose_name='Pontos de Vida')),
                ('CD', models.IntegerField(verbose_name='Classe de Dificuldade')),
            ],
            options={
                'verbose_name': 'Estatística de Criatura Lacaio',
                'verbose_name_plural': 'Estatísticas de Criaturas Lacaios',
                'ordering': ['nd'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EstatisticaCriaturaSolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nd', models.CharField(max_length=10)),
                ('ataque', models.CharField(max_length=10)),
                ('dano', models.CharField(max_length=10)),
                ('defesa', models.CharField(max_length=10)),
                ('res_forte_80', models.CharField(max_length=10, verbose_name='Resistência Forte (80%)')),
                ('res_media_50', models.CharField(max_length=10, verbose_name='Resistência Média (50%)')),
                ('res_fraca_20', models.CharField(max_length=10, verbose_name='Resistência Fraca (20%)')),
                ('pv', models.IntegerField(verbose_name='Pontos de Vida')),
                ('CD', models.IntegerField(verbose_name='Classe de Dificuldade')),
            ],
            options={
                'verbose_name': 'Estatística de Criatura Solo',
                'verbose_name_plural': 'Estatísticas de Criaturas Solo',
                'ordering': ['nd'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadeArma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('requisitos', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('combate', 'Combate'), ('especial', 'Especial'), ('magica', 'Mágica'), ('racial', 'Racial')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadeCriatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('especial', 'Especial'), ('magica', 'Mágica'), ('passiva', 'Passiva'), ('reacao', 'Reação')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemGeral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('modificadores', models.JSONField(blank=True, default=dict)),
                ('categoria', models.CharField(choices=[('consumivel', 'Consumível'), ('ferramenta', 'Ferramenta'), ('servico', 'Serviço'), ('alimento', 'Alimento'), ('animal', 'Animal'), ('veiculo', 'Veículo'), ('tesouro', 'Tesouro'), ('outro', 'Outro')], default='consumivel', max_length=20)),
                ('quantidade', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('classe', models.CharField(choices=[('arcana', 'Arcana'), ('divina', 'Divina'), ('universal', 'Universal')], default='arcana', max_length=20)),
                ('circulo', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('escola', models.CharField(choices=[('abjuracao', 'Abjuração'), ('adivinhacao', 'Adivinhação'), ('convocacao', 'Convocação'), ('encantamento', 'Encantamento'), ('evocacao', 'Evocação'), ('ilusao', 'Ilusão'), ('necromancia', 'Necromancia'), ('transmutacao', 'Transmutação'), ('universal', 'Universal')], max_length=20)),
                ('execucao', models.CharField(max_length=50)),
                ('alcance', models.CharField(max_length=50)),
                ('alvo', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('efeito', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao', models.CharField(max_length=50)),
                ('resistencia', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField()),
                ('aprimoramentos', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialEspecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('modificador', models.CharField(max_length=100)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tipo_item', models.CharField(max_length=20)),
                ('raridade', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Melhoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('arma', 'Arma'), ('armadura', 'Armadura'), ('acessorio', 'Acessório'), ('universal', 'Universal')], max_length=50)),
                ('nivel', models.PositiveSmallIntegerField(default=1)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('requisitos', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pericia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField()),
                ('atributo', models.CharField(choices=[('FOR', 'Força'), ('DES', 'Destreza'), ('CON', 'Constituição'), ('INT', 'Inteligência'), ('SAB', 'Sabedoria'), ('CAR', 'Carisma')], max_length=3)),
                ('treinada', models.BooleanField(default=False)),
                ('penalidade_armadura', models.BooleanField(default=True)),
                ('lista', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='PerigoComplexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=10)),
                ('objetivo', models.TextField()),
                ('efeitos', models.JSONField(default=list)),
                ('acoes', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Pocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rollMin', models.IntegerField()),
                ('rollMax', models.IntegerField()),
                ('tipo', models.CharField(choices=[('oleo', 'Óleo'), ('granada', 'Granada'), ('pocao', 'Poção'), ('outro', 'Outro')], default='pocao', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pocoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.IntegerField()),
                ('rollMin', models.IntegerField()),
                ('rollMax', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('combate', 'Combate'), ('destino', 'Destino'), ('magia', 'Magia'), ('concedido', 'Concedido'), ('tormenta', 'Tormenta'), ('racial', 'Racial'), ('magia/aprimoramento', 'Magia/Aprimoramento'), ('concedido/Aharadak', 'Concedido/Aharadak'), ('concedido/Thwor, Valkaria', 'Concedido/Thwor, Valkaria'), ('concedido/Oceano', 'Concedido/Oceano'), ('concedido/Hyninn', 'Concedido/Hyninn'), ('concedido/Valkaria', 'Concedido/Valkaria'), ('concedido/Sszzaas', 'Concedido/Sszzaas'), ('concedido/Lena,Thyatis', 'Concedido/Lena,Thyatis'), ('concedido/Kally', 'Concedido/Kally'), ('concedido/Marah', 'Concedido/Marah'), ('concedido/Lena', 'Concedido/Lena'), ('concedido/Wynna', 'Concedido/Wynna'), ('concedido/Tenebra', 'Concedido/Tenebra'), ('concedido/Allihanna', 'Concedido/Allihanna'), ('concedido/Tanna-Toh', 'Concedido/Tanna-Toh'), ('concedido/Arsenal', 'Concedido/Arsenal'), ('concedido/Arsenal, Khalmyr, Lin-Wu, Valkaria', 'Concedido/Arsenal, Khalmyr, Lin-Wu, Valkaria'), ('concedido/Azgher', 'Concedido/Azgher'), ('concedido/Aharadak, Nimb', 'Concedido/Aharadak, Nimb'), ('concedido/Megalokk, Thwor', 'Concedido/Megalokk, Thwor'), ('concedido/Nimb', 'Concedido/Nimb'), ('concedido/Megalokk', 'Concedido/Megalokk'), ('concedido/Lin-Wu', 'Concedido/Lin-Wu'), ('concedido/Thyatis', 'Concedido/Thyatis'), ('concedido/Khalmyr', 'Concedido/Khalmyr')], max_length=50)),
                ('requisitos', models.TextField(blank=True, null=True)),
                ('acao', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Poder',
                'verbose_name_plural': 'Poderes',
                'ordering': ['tipo', 'nome'],
            },
        ),
        migrations.CreateModel(
            name='Portas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('rd', models.CharField(max_length=10)),
                ('pv', models.CharField(max_length=10)),
                ('cd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecompensasArmaduras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_percent', models.CharField(db_column='d%', max_length=10)),
                ('item', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recompensas_armaduras',
            },
        ),
        migrations.CreateModel(
            name='RecompensasArmadurasSuperiores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_percent', models.CharField(db_column='d%', max_length=10)),
                ('melhoria', models.TextField()),
            ],
            options={
                'db_table': 'recompensas_armaduras_superiores',
            },
        ),
        migrations.CreateModel(
            name='ServicosHospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField(default=0)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(blank=True, choices=[('comum', 'Comum'), ('confortavel', 'Confortável'), ('luxuosa', 'Luxuosa')], help_text='Tipo de hospedagem (derivado do nome)', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicosOutros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField(default=0)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(blank=True, choices=[('transporte', 'Transporte'), ('saude', 'Saúde'), ('magia', 'Magia'), ('mensagem', 'Mensagem'), ('outro', 'Outro')], help_text='Categoria do serviço (derivado do nome)', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trejeito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('voz', 'Voz'), ('movimento', 'Movimento'), ('habito', 'Hábito'), ('expressao', 'Expressão Facial')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField(default=0)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vestuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('espacos', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Criatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('tipo', models.CharField(choices=[('solo', 'Solo'), ('lacaio', 'Lacaio'), ('especial', 'Especial'), ('chefe', 'Chefe')], max_length=20)),
                ('nivel', models.PositiveSmallIntegerField()),
                ('atributos', models.JSONField()),
                ('tesouro', models.JSONField(default=dict)),
                ('habilidades', models.ManyToManyField(to='t20.habilidadecriatura')),
            ],
        ),
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('origem', models.CharField(choices=[('T20', 'Tormenta 20'), ('Ghanor', 'Ghanor'), ('Ameacas', 'Ameaças de Arton'), ('Deuses', 'Deuses e Heróis')], default='T20', max_length=20)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('modificadores', models.JSONField(blank=True, default=dict)),
                ('classe', models.CharField(choices=[('simples', 'Simples'), ('marcial', 'Marcial'), ('exotica', 'Exótica'), ('fogo', 'Arma de Fogo'), ('simples/corpo-a-corpo', 'Simples Corpo-a-Corpo'), ('simples/distancia', 'Simples Distância'), ('marcial/corpo-a-corpo', 'Marcial Corpo-a-Corpo'), ('marcial/distancia', 'Marcial Distância'), ('exotica/corpo-a-corpo', 'Exótica Corpo-a-Corpo'), ('exotica/distancia', 'Exótica Distância')], default='simples', max_length=25)),
                ('tipo', models.CharField(choices=[('perfuracao', 'Perfuração'), ('corte', 'Corte'), ('impacto', 'Impacto'), ('distancia', 'Distância'), ('corte ou perfuracao', 'Corte ou Perfuração')], max_length=25)),
                ('empunhadura', models.CharField(choices=[('uma_mao', 'Uma mão'), ('duas_maos', 'Duas mãos'), ('leve', 'Leve'), ('arremesso', 'Arremesso')], default='uma_mao', max_length=25)),
                ('dano', models.CharField(help_text='Dados de dano (ex: 1d6, 2d4, etc)', max_length=35)),
                ('critico', models.CharField(default='x2', help_text='Multiplicador de crítico (ex: x2, x3)', max_length=25)),
                ('ameaca', models.PositiveSmallIntegerField(blank=True, help_text='Valor mínimo no d20 para ameaça de crítico (ex: 19, 20)', null=True)),
                ('alcance', models.CharField(blank=True, help_text='Alcance da arma (curto, médio, longo, etc)', max_length=35, null=True)),
                ('espacos', models.DecimalField(decimal_places=1, default=1.0, help_text='Espaços que a arma ocupa no inventário', max_digits=3)),
                ('habilidades', models.ManyToManyField(blank=True, related_name='armas', to='t20.habilidadearma')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armas', to='t20.materialespecial')),
            ],
            options={
                'verbose_name': 'Arma',
                'verbose_name_plural': 'Armas',
                'ordering': ['classe', 'nome'],
            },
        ),
        migrations.CreateModel(
            name='MaterialEspecialPreco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arma', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('armaduraLeve', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('armaduraPesada', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('escudo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('esotericos', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('material', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='precos', to='t20.materialespecial')),
            ],
        ),
    ]
