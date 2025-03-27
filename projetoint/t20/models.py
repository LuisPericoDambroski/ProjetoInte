from django.db import models
from django.core.validators import MinValueValidator

class CategoriaBase(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(0)]
    )
    origem = models.CharField(
        max_length=20,
        choices=[
            ('T20', 'Tormenta 20'),
            ('Ghanor', 'Ghanor'),
            ('Ameacas', 'Ameaças de Arton')
        ],
        default='T20'
    )
    peso = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        abstract = True
        app_label = 't20'

    def __str__(self):
        return self.nome

class Acessorio(CategoriaBase):
    TIPO_CHOICES = [
        ('menor', 'Menor'),
        ('medio', 'Médio'),
        ('maior', 'Maior')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

class Armadura(CategoriaBase):
    CLASSE_CHOICES = [
        ('leve', 'Leve'),
        ('pesada', 'Pesada'),
        ('escudo', 'Escudo')
    ]
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)
    bonus_defesa = models.IntegerField(default=0)  # Valor padrão adicionado
    penalidade = models.IntegerField(default=0)
    modificadores = models.TextField(blank=True, null=True)

class Arma(CategoriaBase):
    CLASSE_CHOICES = [
        ('simples', 'Simples'),
        ('marcial', 'Marcial'),
        ('exotica', 'Exótica')
    ]
    TIPO_CHOICES = [
        ('perfuracao', 'Perfuração'),
        ('corte', 'Corte'),
        ('impacto', 'Impacto')
    ]
    EMPUNHADURA_CHOICES = [
        ('uma-mao', 'Uma mão'),
        ('duas-maos', 'Duas mãos'),
        ('leve', 'Leve')
    ]
    
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)  # Tamanho aumentado
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  # Tamanho aumentado
    empunhadura = models.CharField(max_length=20, choices=EMPUNHADURA_CHOICES)  # Tamanho aumentado
    dano = models.CharField(max_length=20)
    critico = models.CharField(max_length=20)  # Tamanho aumentado
    alcance = models.CharField(max_length=20, blank=True, null=True)
    material = models.ForeignKey('MaterialEspecial', null=True, blank=True, on_delete=models.SET_NULL)
    melhorias = models.ManyToManyField('Melhoria', blank=True)

class ItemGeral(CategoriaBase):
    categoria = models.CharField(max_length=50, blank=True, null=True)

class Esoterico(CategoriaBase):
    TIPO_CHOICES = [
        ('encantamento', 'Encantamento'),
        ('pocao', 'Poção'),
        ('material', 'Material Especial')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.IntegerField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(1)]
    )
    requisitos = models.TextField(blank=True, null=True)

class Alquimico(CategoriaBase):
    TIPO_CHOICES = [
        ('preparado', 'Preparado'),
        ('catalisador', 'Catalisador'),
        ('veneno', 'Veneno')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nivel = models.IntegerField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(1)]
    )
    duracao = models.CharField(max_length=50, blank=True, null=True)
    efeito = models.TextField(blank=True, null=True)

class Melhoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    TIPO_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
        ('escudo', 'Escudo'),
        ('esoterico', 'Esotérico'),
        ('ferramenta', 'Ferramenta'),
        ('vestuario', 'Vestuário'),
        ('qualquer', 'Qualquer')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    custo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(0)]
    )
    requisitos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Magia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    CLASSE_CHOICES = [
        ('arcana', 'Arcana'),
        ('divina', 'Divina'),
        ('universal', 'Universal')
    ]
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)
    ESCOLA_CHOICES = [
        ('abjuracao', 'Abjuração'),
        ('adivinhacao', 'Adivinhação'),
        ('convocacao', 'Convocação'),
        ('encantamento', 'Encantamento'),
        ('evocacao', 'Evocação'),
        ('ilusao', 'Ilusão'),
        ('necromancia', 'Necromancia'),
        ('transmutacao', 'Transmutação')
    ]
    escola = models.CharField(max_length=20, choices=ESCOLA_CHOICES)
    ciclo = models.IntegerField(validators=[MinValueValidator(1)])
    acao = models.CharField(max_length=50)
    alcance = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    alvo = models.CharField(max_length=100)
    aprimoramentos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Poder(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    TIPO_CHOICES = [
        ('combate', 'Combate'),
        ('destino', 'Destino'),
        ('magia', 'Magia'),
        ('concedido', 'Concedido')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    requisitos = models.TextField(blank=True, null=True)
    deuses = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Condicao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    efeitos = models.TextField()
    cura = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class MaterialEspecial(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modificador = models.CharField(max_length=50)
    custo = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    tipo_item = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Veiculo(CategoriaBase):
    TIPO_CHOICES = [
        ('terrestre', 'Terrestre'),
        ('aquatico', 'Aquático'),
        ('aereo', 'Aéreo')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    capacidade = models.IntegerField(validators=[MinValueValidator(1)])
    velocidade = models.CharField(max_length=50)
    tripulacao = models.IntegerField(blank=True, null=True)

class Armadilha(CategoriaBase):
    nivel = models.IntegerField(validators=[MinValueValidator(1)])
    efeito = models.TextField()
    magica = models.BooleanField(default=False)
    cd_resistencia = models.IntegerField(validators=[MinValueValidator(1)])
    gatilho = models.CharField(max_length=100, blank=True, null=True)

class Doenca(CategoriaBase):
    sintomas = models.TextField()
    tratamento = models.TextField(blank=True, null=True)
    tempo_incubacao = models.CharField(max_length=50, blank=True, null=True)