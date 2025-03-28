from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CategoriaBase(models.Model):
    ORIGEM_CHOICES = [
        ('T20', 'Tormenta 20'),
        ('Ghanor', 'Ghanor'),
        ('Ameacas', 'Ameaças de Arton'),
        ('Deuses', 'Deuses e Heróis')
    ]
    
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0)]
    )
    origem = models.CharField(
        max_length=20,
        choices=ORIGEM_CHOICES,
        default='T20'
    )
    peso = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    modificadores = models.JSONField(default=dict, blank=True)

    class Meta:
        abstract = True
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.get_origem_display()})"

class Acessorio(CategoriaBase):
    TIPO_CHOICES = [
        ('menor', 'Menor'),
        ('medio', 'Médio'),
        ('maior', 'Maior'),
        ('unico', 'Único')
    ]
    
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='medio'
    )
    slots = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(3)]
    )

class Armadura(CategoriaBase):
    CLASSE_CHOICES = [
        ('leve', 'Leve'),
        ('pesada', 'Pesada'),
        ('escudo', 'Escudo'),
        ('roupa', 'Vestuário')
    ]
    
    classe = models.CharField(
        max_length=20,
        choices=CLASSE_CHOICES,
        default='leve'
    )
    bonus_defesa = models.IntegerField(default=0)
    penalidade = models.IntegerField(default=0)
    slots = models.PositiveSmallIntegerField(default=1)

class Arma(CategoriaBase):
    CLASSE_CHOICES = [
        ('simples', 'Simples'),
        ('marcial', 'Marcial'),
        ('exotica', 'Exótica'),
        ('unica', 'Única')
    ]
    
    TIPO_CHOICES = [
        ('perfuracao', 'Perfuração'),
        ('corte', 'Corte'),
        ('impacto', 'Impacto'),
        ('distancia', 'Distância')
    ]
    
    EMPUNHADURA_CHOICES = [
        ('uma_mao', 'Uma mão'),
        ('duas_maos', 'Duas mãos'),
        ('leve', 'Leve'),
        ('arremesso', 'Arremesso')
    ]
    
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    empunhadura = models.CharField(max_length=20, choices=EMPUNHADURA_CHOICES)
    dano = models.CharField(max_length=30)
    critico = models.CharField(max_length=20)
    alcance = models.CharField(max_length=30, blank=True, null=True)
    material = models.ForeignKey(
        'MaterialEspecial',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='armas'
    )
    habilidades = models.ManyToManyField(
        'HabilidadeArma',
        blank=True,
        related_name='armas'
    )

class ItemGeral(CategoriaBase):
    CATEGORIA_CHOICES = [
        ('consumivel', 'Consumível'),
        ('ferramenta', 'Ferramenta'),
        ('servico', 'Serviço'),
        ('alimento', 'Alimento'),
        ('animal', 'Animal'),
        ('veiculo', 'Veículo'),
        ('tesouro', 'Tesouro'),
        ('outro', 'Outro')
    ]
    
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='consumivel'
    )
    quantidade = models.PositiveIntegerField(default=1)

class Esoterico(CategoriaBase):
    TIPO_CHOICES = [
        ('encantamento', 'Encantamento'),
        ('pocao', 'Poção'),
        ('material', 'Material'),
        ('pergaminho', 'Pergaminho'),
        ('runico', 'Rúnico'),
        ('reliquia', 'Relíquia')
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    requisitos = models.TextField(blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True, null=True)

class Alquimico(CategoriaBase):
    TIPO_CHOICES = [
        ('preparado', 'Preparado'),
        ('catalisador', 'Catalisador'),
        ('veneno', 'Veneno'),
        ('oleo', 'Óleo'),
        ('extrato', 'Extrato'),
        ('essencia', 'Essência')
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    ingredientes = models.TextField(blank=True, null=True)
    tempo_preparo = models.CharField(max_length=50, blank=True, null=True)

class MaterialEspecial(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    modificador = models.CharField(max_length=100)
    custo = models.DecimalField(max_digits=15, decimal_places=2)
    tipo_item = models.CharField(max_length=20)
    raridade = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

class HabilidadeArma(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    requisitos = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=[
        ('combate', 'Combate'),
        ('especial', 'Especial'),
        ('magica', 'Mágica'),
        ('racial', 'Racial')
    ])

class Melhoria(models.Model):
    TIPO_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
        ('acessorio', 'Acessório'),
        ('universal', 'Universal')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.PositiveSmallIntegerField(default=1)
    custo = models.DecimalField(max_digits=15, decimal_places=2)
    requisitos = models.TextField(blank=True, null=True)

class Encantamento(models.Model):
    TIPO_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
        ('acessorio', 'Acessório')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.PositiveSmallIntegerField()
    efeito = models.JSONField()

class Condicao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    efeitos = models.TextField()
    cura = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=[
        ('fisica', 'Física'),
        ('mental', 'Mental'),
        ('magica', 'Mágica'),
        ('doenca', 'Doença'),
        ('veneno', 'Veneno')
    ])

class Pericia(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    atributo = models.CharField(max_length=3, choices=[
        ('FOR', 'Força'),
        ('DES', 'Destreza'),
        ('CON', 'Constituição'),
        ('INT', 'Inteligência'),
        ('SAB', 'Sabedoria'),
        ('CAR', 'Carisma')
    ])
    treinada = models.BooleanField(default=False)
    penalidade_armadura = models.BooleanField(default=True)

class Magia(models.Model):
    ESCOLA_CHOICES = [
        ('abjuracao', 'Abjuração'),
        ('adivinhacao', 'Adivinhação'),
        ('convocacao', 'Convocação'),
        ('encantamento', 'Encantamento'),
        ('evocacao', 'Evocação'),
        ('ilusao', 'Ilusão'),
        ('necromancia', 'Necromancia'),
        ('transmutacao', 'Transmutação'),
        ('universal', 'Universal')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    escola = models.CharField(max_length=20, choices=ESCOLA_CHOICES)
    circulo = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    componentes = models.CharField(max_length=100)
    alcance = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    aprimoramentos = models.JSONField(default=list)

class Poder(models.Model):
    TIPO_CHOICES = [
        ('combate', 'Combate'),
        ('destino', 'Destino'),
        ('magia', 'Magia'),
        ('concedido', 'Concedido'),
        ('tormenta', 'Tormenta'),
        ('racial', 'Racial')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    requisitos = models.TextField(blank=True, null=True)
    acao = models.CharField(max_length=50, blank=True, null=True)

class Aparencia(models.Model):
    descricao = models.TextField()
    origem = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=[
        ('fisica', 'Física'),
        ('vestimenta', 'Vestimenta'),
        ('marcas', 'Marcas Corporais'),
        ('acessorio', 'Acessório')
    ])

class Trejeito(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=[
        ('voz', 'Voz'),
        ('movimento', 'Movimento'),
        ('habito', 'Hábito'),
        ('expressao', 'Expressão Facial')
    ])

class Criatura(models.Model):
    TIPO_CHOICES = [
        ('solo', 'Solo'),
        ('lacaio', 'Lacaio'),
        ('especial', 'Especial'),
        ('chefe', 'Chefe')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.PositiveSmallIntegerField()
    atributos = models.JSONField()  # Ex: {'FOR': 18, 'DES': 12, ...}
    habilidades = models.ManyToManyField('HabilidadeCriatura')
    tesouro = models.JSONField(default=dict)  # Ex: {'itens': [...], 'tibares': 500}

class HabilidadeCriatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=[
        ('especial', 'Especial'),
        ('magica', 'Mágica'),
        ('passiva', 'Passiva'),
        ('reacao', 'Reação')
    ])

class Armadilha(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    nivel = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=20, choices=[
        ('mecanica', 'Mecânica'),
        ('magica', 'Mágica'),
        ('hibrida', 'Híbrida')
    ])
    efeito = models.TextField()
    cd = models.PositiveSmallIntegerField(verbose_name="CD de Resistência")
    gatilho = models.CharField(max_length=100)

class Doenca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    sintomas = models.TextField()
    tratamento = models.TextField(blank=True, null=True)
    tempo_incubacao = models.CharField(max_length=50, blank=True, null=True)
    cd = models.PositiveSmallIntegerField(verbose_name="CD de Resistência")