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
        max_digits=15,
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

class MaterialEspecial(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    modificador = models.CharField(max_length=100, blank=True, null=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tipo_item = models.CharField(max_length=50, default='arma')
    raridade = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.nome

class MaterialEspecialPreco(models.Model):
    material = models.OneToOneField(
        'MaterialEspecial',
        on_delete=models.CASCADE,
        related_name='precos',
        primary_key=True
    )
    arma = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    armaduraLeve = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    armaduraPesada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    escudo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    esotericos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"Preços para {self.material.nome}"


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

class Armadura(models.Model):
    CLASSE_CHOICES = [
        ('leve', 'Leve'),
        ('pesada', 'Pesada'),
        ('escudo', 'Escudo'),
        ('roupa', 'Vestuário')
    ]
    
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.CharField(max_length=10)
    penalidade = models.IntegerField()
    espacos = models.IntegerField()
    descricao = models.TextField()

class Arma(CategoriaBase):
    CLASSE_CHOICES = [
        ('simples', 'Simples'),
        ('marcial', 'Marcial'),
        ('exotica', 'Exótica'),
        ('fogo', 'Arma de Fogo'),
        ('simples/corpo-a-corpo', 'Simples Corpo-a-Corpo'),
        ('simples/distancia', 'Simples Distância'),
        ('marcial/corpo-a-corpo', 'Marcial Corpo-a-Corpo'),
        ('marcial/distancia', 'Marcial Distância'),
        ('exotica/corpo-a-corpo', 'Exótica Corpo-a-Corpo'),
        ('exotica/distancia', 'Exótica Distância')
    ]
    
    TIPO_CHOICES = [
        ('perfuracao', 'Perfuração'),
        ('corte', 'Corte'),
        ('impacto', 'Impacto'),
        ('distancia', 'Distância'),
        ('corte ou perfuracao', 'Corte ou Perfuração')
    ]
    
    EMPUNHADURA_CHOICES = [
        ('uma_mao', 'Uma mão'),
        ('duas_maos', 'Duas mãos'),
        ('leve', 'Leve'),
        ('arremesso', 'Arremesso')
    ]
    
    # Campos principais
    classe = models.CharField(
        max_length=25,
        choices=CLASSE_CHOICES,
        default='simples'
    )
    tipo = models.CharField(
        max_length=25,
        choices=TIPO_CHOICES
    )
    empunhadura = models.CharField(
        max_length=25,
        choices=EMPUNHADURA_CHOICES,
        default='uma_mao'
    )
    dano = models.CharField(
        max_length=35,
        help_text="Dados de dano (ex: 1d6, 2d4, etc)"
    )
    critico = models.CharField(
        max_length=25,
        default='x2',
        help_text="Multiplicador de crítico (ex: x2, x3)"
    )
    ameaca = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        help_text="Valor mínimo no d20 para ameaça de crítico (ex: 19, 20 ou '—')"
    )
    alcance = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        help_text="Alcance da arma (curto, médio, longo, etc)"
    )
    espacos = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.0,
        help_text="Espaços que a arma ocupa no inventário"
    )
    
    # Relacionamentos
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

    class Meta:
        verbose_name = "Arma"
        verbose_name_plural = "Armas"
        ordering = ['classe', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.get_classe_display()})"
    

class ArmaRandom(models.Model):
    nome = models.CharField(max_length=100)
    chances = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    quantidade = models.PositiveSmallIntegerField(
        blank=True, 
        null=True,
        help_text="Quantidade para itens como flechas, balas, etc."
    )
    origem = models.CharField(
        max_length=20,
        choices=CategoriaBase.ORIGEM_CHOICES,  # Acessando via CategoriaBase
        default='T20'
    )

    def __str__(self):
        return f"{self.nome} ({self.chances}%)"
    
class ArmaduraRandom(models.Model):
    nome = models.CharField(max_length=100)
    chances = models.IntegerField(default=0)
    quantidade = models.IntegerField(null=True, blank=True)
    origem = models.CharField(
        max_length=20, 
        choices=CategoriaBase.ORIGEM_CHOICES,  # Acessando via CategoriaBase
        default='T20'
    )
    
    def __str__(self):
        return self.nome
    

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




class Melhoria(models.Model):
    TIPO_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
        ('acessorio', 'Acessório'),
        ('universal', 'Universal')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
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
    nome = models.CharField(max_length=100)
    detalhes = models.JSONField()  # Armazena o objeto completo com efeito e descricao

    class Meta:
        verbose_name = "Condição"

class Pericia(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    atributo = models.CharField(max_length=20, choices=[  # Aumentado de 3 para 20
        ('FOR', 'Força'),
        ('DES', 'Destreza'),
        ('CON', 'Constituição'),
        ('INT', 'Inteligência'),
        ('SAB', 'Sabedoria'),
        ('CAR', 'Carisma')
    ])
    treinada = models.BooleanField(default=False)
    penalidade_armadura = models.BooleanField(default=True)
    lista = models.JSONField(default=list)


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
    
    # Novos campos adicionados
    CLASSE_CHOICES = [
        ('arcana', 'Arcana'),
        ('divina', 'Divina'),
        ('universal', 'Universal')
    ]
    
    nome = models.CharField(max_length=100, unique=True)
    # Novo campo
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES, default='arcana')
    circulo = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    escola = models.CharField(max_length=20, choices=ESCOLA_CHOICES)
    # Novos campos
    execucao = models.CharField(max_length=50)
    alcance = models.CharField(max_length=100)
    alvo = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    efeito = models.CharField(max_length=100, blank=True, null=True)
    duracao = models.CharField(max_length=1000)
    resistencia = models.CharField(max_length=1000, blank=True, null=True)
    descricao = models.TextField()
    aprimoramentos = models.JSONField(default=list)

    def __str__(self):
        return f"{self.nome} ({self.get_classe_display()} {self.circulo}º)"
    
class TipoPoder(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Poder(models.Model):
    TIPO_CHOICES = [
        ('combate', 'Combate'),
        ('destino', 'Destino'),
        ('magia', 'Magia'),
        ('concedido', 'Concedido'),
        ('tormenta', 'Tormenta'),
        ('racial', 'Racial'),
        # ... (keep your existing choices)
    ]
    
    # Campos básicos
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    acao = models.CharField(max_length=50, blank=True, null=True)
    custo_pm = models.PositiveSmallIntegerField(null=True, blank=True)
    magia = models.BooleanField(default=False)
    
    # Requisitos de atributos
    requisito_forca = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_destreza = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_constituicao = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_inteligencia = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_sabedoria = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_carisma = models.PositiveSmallIntegerField(null=True, blank=True)
    
    # Outros requisitos
    requisito_nivel = models.PositiveSmallIntegerField(null=True, blank=True)
    requisito_pericias = models.ManyToManyField(
        'Pericia',
        blank=True,
        related_name='poderes_requeridos'
    )
    requisito_poderes = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='requerido_por'
    )
    requisito_outros = models.TextField(blank=True, null=True)
    
    # Campos para aprimoramentos (se aplicável)
    aprimoramentos = models.JSONField(default=list, blank=True)
    
    class Meta:
        verbose_name = "Poder"
        verbose_name_plural = "Poderes"
        ordering = ['tipo', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    def get_requisitos_texto(self):
        """Retorna os requisitos formatados para exibição"""
        requisitos = []
        
        # Atributos
        atributos = [
            ('FOR', self.requisito_forca),
            ('DES', self.requisito_destreza),
            ('CON', self.requisito_constituicao),
            ('INT', self.requisito_inteligencia),
            ('SAB', self.requisito_sabedoria),
            ('CAR', self.requisito_carisma)
        ]
        
        req_atributos = [f"{nome} {valor}" for nome, valor in atributos if valor]
        if req_atributos:
            requisitos.append(", ".join(req_atributos))
        
        # Nível
        if self.requisito_nivel:
            requisitos.append(f"{self.requisito_nivel}º nível")
        
        # Perícias
        if self.requisito_pericias.exists():
            pericias = [p.nome for p in self.requisito_pericias.all()]
            requisitos.append(f"Treinado em {', '.join(pericias)}")
        
        # Poderes
        if self.requisito_poderes.exists():
            poderes = [p.nome for p in self.requisito_poderes.all()]
            requisitos.append(f"Poderes: {', '.join(poderes)}")
        
        # Outros
        if self.requisito_outros:
            requisitos.append(self.requisito_outros)
        
        return "; ".join(requisitos) if requisitos else "Nenhum"

class Trejeito(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=[
        ('voz', 'Voz'),
        ('movimento', 'Movimento'),
        ('habito', 'Hábito'),
        ('expressao', 'Expressão Facial')
    ])


class Armadilha(models.Model):
    nome = models.CharField(max_length=100)
    efeito = models.TextField()
    resistencia = models.CharField(max_length=100)
    investigacao = models.CharField(max_length=100)
    magica = models.BooleanField()
    nivel = models.CharField(max_length=10)

class Doenca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    sintomas = models.TextField()
    tratamento = models.TextField(blank=True, null=True)
    tempo_incubacao = models.CharField(max_length=50, blank=True, null=True)
    cd = models.PositiveSmallIntegerField(verbose_name="CD de Resistência")

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField(default=0)
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class Alimentacao(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.DecimalField(max_digits=3, decimal_places=1)
    descricao = models.TextField()

class AlquimicoCatalisador(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.DecimalField(max_digits=3, decimal_places=1)
    descricao = models.TextField()

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField(default=0)
    descricao = models.TextField()



class EsotericoRandom(models.Model):
    nome = models.CharField(max_length=100)
    chances = models.PositiveSmallIntegerField()


    
class Clima(models.Model):
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()

class EncantoArmadura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class EncantoArma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class ErroCritico(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)  # Armazena "1", "2", etc
    descricao = models.TextField()

    class Meta:
        verbose_name = "Erro Crítico"

class BaseEstatisticaCriatura(models.Model):
    """Classe abstrata base para todas as estatísticas de criaturas"""
    nd = models.CharField(max_length=10)
    ataque = models.CharField(max_length=10)
    dano = models.CharField(max_length=10)
    defesa = models.CharField(max_length=10)
    res_forte_80 = models.CharField(max_length=10, verbose_name="Resistência Forte (80%)")
    res_media_50 = models.CharField(max_length=10, verbose_name="Resistência Média (50%)")
    res_fraca_20 = models.CharField(max_length=10, verbose_name="Resistência Fraca (20%)")
    pv = models.IntegerField(verbose_name="Pontos de Vida")
    CD = models.IntegerField(verbose_name="Classe de Dificuldade")

    class Meta:
        abstract = True
        ordering = ['nd']

    def __str__(self):
        return f"{self.__class__._meta.verbose_name} ND {self.nd}"


class EstatisticaCriaturaEspecial(BaseEstatisticaCriatura):
    TIPO_CHOICES = [
        ('combate', 'Combate'),
        ('magico', 'Mágico'),
        ('suporte', 'Suporte'),
        ('chefe', 'Chefe')
    ]
    
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='combate',
        help_text="Tipo especial da criatura"
    )

    class Meta(BaseEstatisticaCriatura.Meta):
        verbose_name = "Estatística de Criatura Especial"
        verbose_name_plural = "Estatísticas de Criaturas Especiais"

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

    def __str__(self):
        return self.nome

class HabilidadeCriatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=[
        ('especial', 'Especial'),
        ('magica', 'Mágica'),
        ('passiva', 'Passiva'),
        ('reacao', 'Reação')
    ])

    def __str__(self):
        return self.nome


class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class CustoMagia(models.Model):
    circulo = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        unique=True
    )
    custo = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Custo para {self.circulo}º círculo: {self.custo} PM"






class Vestuario(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class PerigoComplexo(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=10)
    objetivo = models.TextField()
    efeitos = models.JSONField(default=list)
    acoes = models.JSONField(default=list)

    def __str__(self):
        return f"{self.nome} (Nível {self.nivel})"

class Pocao(models.Model):
    TIPO_CHOICES = [
        ('oleo', 'Óleo'),
        ('granada', 'Granada'),
        ('pocao', 'Poção'),
        ('outro', 'Outro')
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    rollMin = models.IntegerField()
    rollMax = models.IntegerField()
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='pocao'
    )

    def __str__(self):
        return self.nome
    


class ServicosOutros(models.Model):
    CATEGORIA_CHOICES = [
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('magia', 'Magia'),
        ('mensagem', 'Mensagem'),
        ('outro', 'Outro')
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField(default=0)
    descricao = models.TextField()
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        blank=True,
        null=True,
        help_text="Categoria do serviço (derivado do nome)"
    )

    def save(self, *args, **kwargs):
        # Auto-preencher a categoria baseado no nome
        if 'condução' in self.nome.lower():
            self.categoria = 'transporte'
        elif 'curandeiro' in self.nome.lower():
            self.categoria = 'saude'
        elif 'magia' in self.nome.lower():
            self.categoria = 'magia'
        elif 'mensageiro' in self.nome.lower():
            self.categoria = 'mensagem'
        else:
            self.categoria = 'outro'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome



class Pocoes(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    rollMin = models.IntegerField()
    rollMax = models.IntegerField()

    def __str__(self):
        return self.nome

class Portas(models.Model):
    tipo = models.CharField(max_length=50)
    rd = models.CharField(max_length=10)
    pv = models.CharField(max_length=10)
    cd = models.IntegerField()

    def __str__(self):
        return self.tipo
class RecompensasArmaduras(models.Model):
    d_percent = models.CharField(max_length=10, db_column='d%')
    item = models.CharField(max_length=100)

    class Meta:
        db_table = 'recompensas_armaduras'
        verbose_name = "Recompensa de Armadura"
        verbose_name_plural = "Recompensas de Armaduras"

    def __str__(self):
        return f"{self.d_percent} - {self.item}"

class RecompensasArmaduras(models.Model):
    d_percent = models.CharField(max_length=10, db_column='d%')
    item = models.CharField(max_length=100)

    class Meta:
        db_table = 'recompensas_armaduras'
        verbose_name = "Recompensa de Armadura"
        verbose_name_plural = "Recompensas de Armaduras"

    def __str__(self):
        return f"{self.d_percent} - {self.item}"

class RecompensasArmadurasSuperiores(models.Model):
    d_percent = models.CharField(max_length=10, db_column='d%')
    melhoria = models.TextField()

    class Meta:
        db_table = 'recompensas_armaduras_superiores'
        verbose_name = "Recompensa de Armadura Superior"
        verbose_name_plural = "Recompensas de Armaduras Superiores"

    def __str__(self):
        return f"{self.d_percent} - {self.melhoria[:50]}..."

class RecompensasArmasSuperiores(models.Model):
    d_percent = models.CharField(max_length=10, db_column='d%')
    melhoria = models.TextField()

    class Meta:
        db_table = 'recompensas_armas_superiores'
        verbose_name = "Recompensa de Arma Superior"
        verbose_name_plural = "Recompensas de Armas Superiores"
        ordering = ['d_percent']

    def __str__(self):
        return f"{self.d_percent} - {self.melhoria[:50]}..."

class RecompensasEsotericosSuperiores(models.Model):
    d_percent = models.CharField(max_length=10, db_column='d%')
    melhoria = models.TextField()

    class Meta:
        db_table = 'recompensas_esotericos_superiores'
        verbose_name = "Recompensa de Esotérico Superior"
        verbose_name_plural = "Recompensas de Esotéricos Superiores"

    def __str__(self):
        return f"{self.d_percent} - {self.melhoria[:50]}..."

class ServicosHospedagem(models.Model):
    TIPO_CHOICES = [
        ('comum', 'Comum'),
        ('confortavel', 'Confortável'),
        ('luxuosa', 'Luxuosa')
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    espacos = models.IntegerField(default=0)
    descricao = models.TextField()
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        blank=True,
        null=True,
        help_text="Tipo de hospedagem (derivado do nome)"
    )

    def save(self, *args, **kwargs):
        # Auto-preencher o tipo baseado no nome
        if 'comum' in self.nome.lower():
            self.tipo = 'comum'
        elif 'confortável' in self.nome.lower() or 'confortavel' in self.nome.lower():
            self.tipo = 'confortavel'
        elif 'luxuosa' in self.nome.lower():
            self.tipo = 'luxuosa'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class BaseEstatisticaCriatura(models.Model):
    """Classe abstrata base para todas as estatísticas de criaturas"""
    nd = models.CharField(max_length=10)
    ataque = models.CharField(max_length=10)
    dano = models.CharField(max_length=10)
    defesa = models.CharField(max_length=10)
    res_forte_80 = models.CharField(max_length=10, verbose_name="Resistência Forte (80%)")
    res_media_50 = models.CharField(max_length=10, verbose_name="Resistência Média (50%)")
    res_fraca_20 = models.CharField(max_length=10, verbose_name="Resistência Fraca (20%)")
    pv = models.IntegerField(verbose_name="Pontos de Vida")
    CD = models.IntegerField(verbose_name="Classe de Dificuldade")

    class Meta:
        abstract = True
        ordering = ['nd']

    def __str__(self):
        return f"{self.__class__._meta.verbose_name} ND {self.nd}"

class EstatisticaCriaturaLacaio(BaseEstatisticaCriatura):
    class Meta(BaseEstatisticaCriatura.Meta):
        verbose_name = "Estatística de Criatura Lacaio"
        verbose_name_plural = "Estatísticas de Criaturas Lacaios"

class EstatisticaCriaturaSolo(BaseEstatisticaCriatura):
    class Meta(BaseEstatisticaCriatura.Meta):
        verbose_name = "Estatística de Criatura Solo"
        verbose_name_plural = "Estatísticas de Criaturas Solo"



    class Meta(BaseEstatisticaCriatura.Meta):
        verbose_name = "Estatística de Criatura Especial"
        verbose_name_plural = "Estatísticas de Criaturas Especiais"

class Aparencia(models.Model):
    TIPO_CHOICES = [
        ('fisica', 'Física'),
        ('vestimenta', 'Vestimenta'),
        ('marcas', 'Marcas/Cicatrizes'),
        ('estilo', 'Estilo'),
        ('outros', 'Outros')
    ]
    
    descricao = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='fisica',
        help_text="Tipo de aparência física"
    )
    origem = models.CharField(
        max_length=20,
        choices=CategoriaBase.ORIGEM_CHOICES,
        default='T20',
        blank=True
    )
    modificadores = models.JSONField(
        default=dict,
        blank=True,
        help_text="Modificadores opcionais que esta aparência pode conceder"
    )

    class Meta:
        verbose_name = "Aparência"
        verbose_name_plural = "Aparências"
        ordering = ['tipo', 'descricao']

    def __str__(self):
        return f"{self.descricao} ({self.get_tipo_display()})"
