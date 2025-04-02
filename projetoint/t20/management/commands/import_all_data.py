import json
import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from t20.models import *

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Importa dados específicos ou todos os dados dos JSONs para os modelos Django'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--arquivos',
            nargs='+',
            type=str,
            help='Lista de arquivos específicos para importar (ex: acessorios.json armas.json)'
        )
        parser.add_argument(
            '--origens',
            nargs='+',
            type=str,
            help='Lista de origens específicas para processar (ex: T20 Ghanor)'
        )
    
    def handle(self, *args, **options):
        base_dir = Path('data')
        sources = {
            'json-t20': 'T20',
            'json-ghanor': 'Ghanor',
            'json-ameacas-arton': 'Ameacas',
            'json-deuses-e-herois': 'Deuses'
        }

        # Filtra as origens se o argumento foi passado
        if options['origens']:
            sources = {k: v for k, v in sources.items() if v in options['origens']}

        for source_dir, origem in sources.items():
            self.stdout.write(self.style.SUCCESS(f'Processando {source_dir}...'))
            self.process_source(base_dir / source_dir, origem, options.get('arquivos'))

    def process_source(self, source_dir, origem, arquivos_selecionados=None):
        processors = {
            'acessorios.json': self.process_acessorios,
            'accessories.json': self.process_acessorios,
            'armaduras.json': self.process_armaduras,
            'armaduras-random.json': self.process_armaduras_random,
            'armas.json': self.process_armas,
            'armas-random.json': self.process_armas_random,
            'armas-habilidades.json': self.process_habilidades_arma,
            'itens-gerais.json': self.process_itens_gerais,
            'alimentacao.json': self.process_alimentacao,
            'ferramentas.json': self.process_ferramentas,
            'veiculos.json': self.process_veiculos,
            'animais.json': self.process_animais,
            'vestuarios.json': self.process_vestuarios,
            'servicos.json': self.process_servicos,
            'esotericos.json': self.process_esotericos,
            'esotericos-random.json': self.process_esotericos_random,
            'alquimicos-preparados.json': self.process_alquimicos_preparados,
            'alquimicos-catalisadores.json': self.process_alquimicos_catalisadores,
            'alquimicos-venenos.json': self.process_alquimicos_venenos,
            'pocoes.json': self.process_pocoes,
            'magias.json': self.process_magias,
            'magias-custos.json': self.process_magias_custos,
            'poderes.json': self.process_poderes,
            'melhorias.json': self.process_melhorias,
            'melhorias-random.json': self.process_melhorias_random,
            'melhorias-precos.json': self.process_melhorias_precos,
            'encantos-armaduras.json': self.process_encantos_armaduras,
            'encantos-armas.json': self.process_encantos_armas,
            'encantos-precos.json': self.process_encantos_precos,
            'materiais-especiais.json': self.process_materiais_especiais,
            'materiais-especiais-precos.json': self.process_materiais_precos,
            'condicoes.json': self.process_condicoes,
            'armadilhas.json': self.process_armadilhas,
            'doencas.json': self.process_doencas,
            'climas.json': self.process_climas,
            'perigos-complexos.json': self.process_perigos_complexos,
            'portas.json': self.process_portas,
            'estatisticas_criaturas_solo.json': lambda d, o: self.process_criaturas(d, o, 'solo'),
            'estatisticas_criaturas_lacaios.json': lambda d, o: self.process_criaturas(d, o, 'lacaio'),
            'estatisticas_criaturas_especiais.json': lambda d, o: self.process_criaturas(d, o, 'especial'),
            'aparencias.json': self.process_aparencias,
            'trejeitos.json': self.process_trejeitos,
            'pericias.json': self.process_pericias,
            'erros_criticos.json': self.process_erros_criticos,
            'recompensas-armaduras.json': self.process_recompensas_armaduras,
            'recompensas-armaduras-superiores.json': self.process_recompensas_armaduras_superiores,
            'recompensas-armas-superiores.json': self.process_recompensas_armas_superiores,
            'recompensas-esotericos-superiores.json': self.process_recompensas_esotericos_superiores,
        }

        if arquivos_selecionados:
            processors = {k: v for k, v in processors.items() if k in arquivos_selecionados}

        self.stdout.write(f"Processadores ativos: {list(processors.keys())}")

        for filename, processor in processors.items():
            file_path = source_dir / filename
                
            if not file_path.exists():
                self.stdout.write(self.style.WARNING(f'Arquivo não encontrado: {filename}'))
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_data = f.read()
                    cleaned_data = raw_data.replace('`', "'")
                    data = json.loads(cleaned_data)
                    
                    if not isinstance(data, list):
                        data = [data]

                    success = 0
                    with transaction.atomic():
                        for item in data:
                            try:
                                processor(item, origem)
                                success += 1
                            except Exception as e:
                                item_id = item.get('d%', item.get('id', 'sem identificador'))
                                self.stdout.write(self.style.ERROR(f'Erro no item {item_id}: {str(e)}'))
                        
                        self.stdout.write(self.style.SUCCESS(f'{filename}: {success}/{len(data)} itens importados'))
            
            except json.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f'Erro ao decodificar JSON em {filename}: {str(e)}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erro ao processar {filename}: {str(e)}'))
            
    
    def process_acessorios(self, item, origem):
        Acessorio.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'tipo': item.get('tipo', 'medio'),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'slots': item.get('slots', 1),
                'modificadores': item.get('modificadores', {})
            }
        )

    def process_armaduras(self, item, origem):
        Armadura.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'classe': item.get('classe', 'leve'),
                'preco': item.get('preco', 0),
                'bonus': item.get('bonus', '0'),
                'penalidade': item.get('penalidade', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_armaduras_random(self, item, origem):
        ArmaduraRandom.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'chances': item.get('chances', 0),
                'quantidade': item.get('quantidade'),
                'origem': origem
            }
        )

    def process_armas(self, item, origem):
        material = None
        if 'material' in item:
            material = MaterialEspecial.objects.filter(nome=item['material']).first()
        
        arma, created = Arma.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'classe': item.get('classe', 'simples'),
                'tipo': item.get('tipo', 'corte'),
                'empunhadura': item.get('empunhadura', 'uma_mao'),
                'dano': item.get('dano', '1d6'),
                'critico': item.get('critico', 'x2'),
                'ameaca': item.get('ameaca'),
                'alcance': item.get('alcance'),
                'espacos': item.get('espacos', 1.0),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'peso': item.get('peso'),
                'origem': origem,
                'material': material
            }
        )
        
        if 'habilidades' in item:
            habilidades = []
            for hab_nome in item['habilidades']:
                hab, _ = HabilidadeArma.objects.get_or_create(
                    nome=hab_nome,
                    defaults={'descricao': '', 'tipo': 'combate'}
                )
                habilidades.append(hab)
            arma.habilidades.set(habilidades)

    def process_habilidades_arma(self, item, origem):
        HabilidadeArma.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'requisitos': item.get('requisitos'),
                'tipo': item.get('tipo', 'combate')
            }
        )

    def process_itens_gerais(self, item, origem):
        ItemGeral.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'categoria': item.get('categoria', 'outro'),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'quantidade': item.get('quantidade', 1)
            }
        )

    def process_alimentacao(self, item, origem):
        Alimentacao.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_ferramentas(self, item, origem):
        Ferramenta.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_veiculos(self, item, origem):
        Veiculo.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_animais(self, item, origem):
        Animal.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_vestuarios(self, item, origem):
        Vestuario.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_servicos(self, item, origem):
        ServicosOutros.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_esotericos(self, item, origem):
        Esoterico.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'tipo': item.get('tipo', 'pocao'),
                'nivel': item.get('nivel', 1),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'requisitos': item.get('requisitos'),
                'duracao': item.get('duracao')
            }
        )

    def process_esotericos_random(self, item, origem):
        EsotericoRandom.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'chances': item.get('chances', 0)
            }
        )

    def process_alquimicos_preparados(self, item, origem):
        Alquimico.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'tipo': 'preparado',
                'nivel': item.get('nivel', 1),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'ingredientes': item.get('ingredientes'),
                'tempo_preparo': item.get('tempo_preparo')
            }
        )

    def process_alquimicos_catalisadores(self, item, origem):
        AlquimicoCatalisador.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'espacos': item.get('espacos', 0),
                'descricao': item.get('descricao', '')
            }
        )

    def process_alquimicos_venenos(self, item, origem):
        Alquimico.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'tipo': 'veneno',
                'nivel': item.get('nivel', 1),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'ingredientes': item.get('ingredientes'),
                'tempo_preparo': item.get('tempo_preparo')
            }
        )

    def process_pocoes(self, item, origem):
        Pocao.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'preco': item.get('preco', 0),
                'rollMin': item.get('rollMin', 0),
                'rollMax': item.get('rollMax', 0),
                'tipo': item.get('tipo', 'pocao')
            }
        )

    def process_magias(self, item, origem):
        Magia.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'classe': item.get('classe', 'arcana'),
                'circulo': item.get('circulo', 1),
                'escola': item.get('escola', 'universal'),
                'execucao': item.get('execucao', ''),
                'alcance': item.get('alcance', ''),
                'alvo': item.get('alvo'),
                'area': item.get('area'),
                'efeito': item.get('efeito'),
                'duracao': item.get('duracao', ''),
                'resistencia': item.get('resistencia'),
                'descricao': item.get('descricao', ''),
                'aprimoramentos': item.get('aprimoramentos', [])
            }
        )

    def process_magias_custos(self, item, origem):
        CustoMagia.objects.update_or_create(
            circulo=item['circulo'],
            defaults={
                'custo': item.get('custo', 0)
            }
        )

    def process_poderes(self, item, origem):
        # Extrair pré-requisitos da descrição
        descricao = item.get('desc', '')
        requisitos = {
            'for': 0, 'des': 0, 'con': 0, 'int': 0, 'sab': 0, 'car': 0,
            'nivel': None, 'pericias': [], 'poderes': [], 'outros': []
        }
        
        # Padrões para extração de atributos
        padroes = [
            (r'For (\d+)', 'for'),
            (r'Des (\d+)', 'des'),
            (r'Con (\d+)', 'con'),
            (r'Int (\d+)', 'int'),
            (r'Sab (\d+)', 'sab'),
            (r'Car (\d+)', 'car'),
            (r'(\d+)º nível', 'nivel')
        ]
        
        # Extrair valores de atributos
        for padrao, campo in padroes:
            match = re.search(padrao, descricao)
            if match:
                requisitos[campo] = int(match.group(1))
        
        # Extrair pré-requisitos textuais
        if 'Pré-requisito:' in descricao or 'Pré-requisitos:' in descricao:
            partes = descricao.split('Pré-requisito')[-1].split('.')[0]
            partes = partes.replace(':', '').strip()
            
            # Separar por vírgulas ou "e"
            for parte in re.split(r', | e ', partes):
                parte = parte.strip()
                if not parte:
                    continue
                    
                # Verificar se é perícia
                if 'treinado' in parte.lower():
                    pericias = parte.replace('treinado em', '').strip()
                    requisitos['pericias'].append(pericias)
                # Verificar se é poder
                elif any(p.lower() in parte.lower() for p in ['poder', 'habilidade']):
                    poderes = parte.replace('poder', '').replace('habilidade', '').strip()
                    requisitos['poderes'].append(poderes)
                else:
                    requisitos['outros'].append(parte)
        
        # Determinar se é uma magia
        is_magia = '(magia)' in descricao.lower()
        
        # Extrair custo PM se existir
        custo_pm = None
        pm_match = re.search(r'gastar (\d+) PM', descricao)
        if pm_match:
            custo_pm = int(pm_match.group(1))
        
        # Criar/atualizar o poder
        Poder.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': descricao,
                'tipo': item.get('tipo', 'combate'),
                'requisito_forca': requisitos['for'] or None,
                'requisito_destreza': requisitos['des'] or None,
                'requisito_constituicao': requisitos['con'] or None,
                'requisito_inteligencia': requisitos['int'] or None,
                'requisito_sabedoria': requisitos['sab'] or None,
                'requisito_carisma': requisitos['car'] or None,
                'requisito_nivel': requisitos['nivel'],
                'requisito_pericias': ', '.join(requisitos['pericias']) if requisitos['pericias'] else None,
                'requisito_poderes': ', '.join(requisitos['poderes']) if requisitos['poderes'] else None,
                'requisito_outros': ', '.join(requisitos['outros']) if requisitos['outros'] else None,
                'acao': item.get('acao'),
                'custo_pm': custo_pm,
                'magia': is_magia
            }
        )

    def process_melhorias(self, item, origem):
        Melhoria.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'tipo': item.get('tipo', 'universal'),
                'nivel': item.get('nivel', 1),
                'custo': item.get('custo', 0),
                'requisitos': item.get('requisitos')
            }
        )

    def process_melhorias_random(self, item, origem):
        pass

    def process_melhorias_precos(self, item, origem):
        pass

    def process_encantos_armaduras(self, item, origem):
        Encantamento.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'tipo': 'armadura',
                'nivel': item.get('nivel', 1),
                'efeito': item.get('efeito', {})
            }
        )

    def process_encantos_armas(self, item, origem):
        Encantamento.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'tipo': 'arma',
                'nivel': item.get('nivel', 1),
                'efeito': item.get('efeito', {})
            }
        )

    def process_encantos_precos(self, item, origem):
        pass

    def process_materiais_especiais(self, item, origem):
        MaterialEspecial.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'modificador': item.get('modificador', ''),
                'custo': item.get('custo', 0),
                'tipo_item': item.get('tipo_item', 'arma'),
                'raridade': item.get('raridade', 1)
            }
        )

    def process_materiais_precos(self, item, origem):
        try:
            # Obtém o nome do material - usa 'nome' pois é o campo presente no JSON
            material_nome = item['nome']
            
            # Verifica se o material existe, caso contrário cria um básico
            material, created = MaterialEspecial.objects.get_or_create(
                nome=material_nome,
                defaults={
                    'descricao': f"Material {material_nome} - criado automaticamente",
                    'modificador': "A ser definido",
                    'custo': 0,
                    'tipo_item': 'universal',
                    'raridade': 3
                }
            )
            
            if created:
                self.stdout.write(self.style.WARNING(f"Material {material_nome} criado automaticamente"))
            
            # Cria ou atualiza os preços do material
            MaterialEspecialPreco.objects.update_or_create(
                material=material,
                defaults={
                    'arma': item.get('arma', 0),
                    'armaduraLeve': item.get('armaduraLeve', 0),
                    'armaduraPesada': item.get('armaduraPesada', 0),
                    'escudo': item.get('escudo', 0),
                    'esotericos': item.get('esotericos', 0)
                }
            )
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao processar material {item.get('nome')}: {str(e)}"))

    def process_condicoes(self, item, origem):
        Condicao.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'detalhes': item.get('detalhes', {})
            }
        )

    def process_armadilhas(self, item, origem):
        magica = item.get('magica', 'nao').lower() == 'sim'
        Armadilha.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'efeito': item.get('efeito', ''),
                'resistencia': item.get('resistencia', ''),
                'investigacao': item.get('investigacao', ''),
                'magica': magica,
                'nivel': item.get('nivel', '1')
            }
        )

    def process_doencas(self, item, origem):
        Doenca.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'sintomas': item.get('sintomas', ''),
                'tratamento': item.get('tratamento'),
                'tempo_incubacao': item.get('tempo_incubacao'),
                'cd': item.get('cd', 10)
            }
        )

    def process_climas(self, item, origem):
        Clima.objects.update_or_create(
            tipo=item['tipo'],
            defaults={
                'descricao': item.get('descricao', '')
            }
        )

    def process_perigos_complexos(self, item, origem):
        PerigoComplexo.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'nivel': item.get('nivel', '1'),
                'objetivo': item.get('objetivo', ''),
                'efeitos': item.get('efeitos', []),
                'acoes': item.get('acoes', [])
            }
        )

    def process_portas(self, item, origem):
        Portas.objects.update_or_create(
            tipo=item['tipo'],
            defaults={
                'rd': item.get('rd', ''),
                'pv': item.get('pv', ''),
                'cd': item.get('cd', 0)
            }
        )

    def process_criaturas(self, item, origem, tipo):
        defaults = {
            'ataque': item.get('ataque', ''),
            'dano': item.get('dano', ''),
            'defesa': item.get('defesa', ''),
            'res_forte_80': item.get('res_forte_80%', ''),
            'res_media_50': item.get('res_media_50%', ''),
            'res_fraca_20': item.get('res_fraca_20%', ''),
            'pv': item.get('pv', 0),
            'CD': item.get('CD', 0)
        }
        
        if tipo == 'lacaio':
            EstatisticaCriaturaLacaio.objects.update_or_create(
                nd=item['nd'],
                defaults=defaults
            )
        elif tipo == 'solo':
            EstatisticaCriaturaSolo.objects.update_or_create(
                nd=item['nd'],
                defaults=defaults
            )
        elif tipo == 'especial':
            defaults['tipo'] = item.get('tipo', 'combate')
            EstatisticaCriaturaEspecial.objects.update_or_create(
                nd=item['nd'],
                defaults=defaults
            )

    def process_aparencias(self, item, origem):
        try:
            if isinstance(item, str):
                Aparencia.objects.get_or_create(
                    descricao=item,
                    defaults={
                        'origem': origem,
                        'tipo': 'outros'
                    }
                )
            elif isinstance(item, dict):
                defaults = {
                    'tipo': item.get('tipo', 'outros'),
                    'origem': item.get('origem', origem),
                    'modificadores': item.get('modificadores', {})
                }
                Aparencia.objects.update_or_create(
                    descricao=item['descricao'],
                    defaults=defaults
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao processar aparência: {str(e)}"))
            if hasattr(self, 'log_error'):
                self.log_error(f"Aparência - {item if isinstance(item, str) else item.get('descricao', 'sem descrição')}: {str(e)}")
    def process_trejeitos(self, item, origem):
        try:
            # Se o item é uma string simples (caso do JSON)
            if isinstance(item, str):
                Trejeito.objects.get_or_create(
                    descricao=item,
                    defaults={'tipo': 'habito'}  # Definindo 'habito' como padrão
                )
            # Se for um dicionário (caso de outros possíveis JSONs)
            elif isinstance(item, dict):
                Trejeito.objects.update_or_create(
                    descricao=item['descricao'],
                    defaults={'tipo': item.get('tipo', 'habito')}
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item if isinstance(item, str) else item.get('descricao', 'sem nome')}: {str(e)}"))

    def process_pericias(self, item, origem):
        Pericia.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item.get('descricao', ''),
                'atributo': item.get('atributo', 'DES'),
                'treinada': item.get('treinada', False),
                'penalidade_armadura': item.get('penalidade_armadura', True),
                'lista': item.get('lista', [])
            }
        )

    def process_erros_criticos(self, item, origem):
        try:
            # Este JSON tem um formato especial onde o item é todo o dicionário
            if isinstance(item, dict):
                for codigo, descricao in item.items():
                    ErroCritico.objects.update_or_create(
                        codigo=codigo,
                        defaults={'descricao': descricao}
                    )
            # Manter a lógica original para outros formatos
            elif isinstance(item, (list, tuple)) or 'codigo' in item:
                codigo = item.get('codigo') or str(item.get('id'))
                if not codigo:
                    raise ValueError("Item sem código identificador")
                    
                ErroCritico.objects.update_or_create(
                    codigo=codigo,
                    defaults={'descricao': item.get('descricao', '')}
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item.get('codigo', 'sem nome')}: {str(e)}"))

    def process_recompensas_armaduras(self, item, origem):
        try:
            # Limpa caracteres problemáticos
            item_data = {k: v.replace('`', "'") if isinstance(v, str) else v for k, v in item.items()}
            RecompensasArmaduras.objects.update_or_create(
                d_percent=item_data['d%'],
                defaults={'item': item_data.get('item', '')}
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item.get('d%')}: {str(e)}"))

    

    def process_armas_random(self, item, origem):
        ArmaRandom.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'chances': item.get('chances', 0),
                'quantidade': item.get('quantidade'),
                'origem': origem
            }
        )
    
    def process_recompensas_armaduras_superiores(self, item, origem):
        try:
            melhoria = item['melhoria']
            if isinstance(melhoria, str):
                melhoria = melhoria.replace('`', "'")  # Substitui crases por aspas simples
            RecompensasArmadurasSuperiores.objects.update_or_create(
                d_percent=item['d%'],
                defaults={'melhoria': melhoria}
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item.get('d%', 'sem identificador')}: {str(e)}"))

    def process_recompensas_armas_superiores(self, item, origem):
        try:
            melhoria = item['melhoria']
            if isinstance(melhoria, str):
                melhoria = melhoria.replace('`', "'")  # Substitui crases por aspas simples
            RecompensasArmasSuperiores.objects.update_or_create(
                d_percent=item['d%'],
                defaults={'melhoria': melhoria}
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item.get('d%', 'sem identificador')}: {str(e)}"))

    def process_recompensas_esotericos_superiores(self, item, origem):
        try:
            melhoria = item['melhoria']
            if isinstance(melhoria, str):
                melhoria = melhoria.replace('`', "'")  # Substitui crases por aspas simples
            RecompensasEsotericosSuperiores.objects.update_or_create(
                d_percent=item['d%'],
                defaults={'melhoria': melhoria}
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro no item {item.get('d%', 'sem identificador')}: {str(e)}"))
    
    def process_deuses(self, item, origem):
        # Handle the subsections structure
        if 'subsections' in item:
            for subsection in item['subsections']:
                if subsection['title'].lower() == 'deus':
                    for deus_item in subsection['items']:
                        self._process_single_deus(deus_item, origem)
        else:
            self._process_single_deus(item, origem)

    def _process_single_deus(self, item, origem):
        Deus.objects.update_or_create(
            title=item['title'],
            defaults={
                'description': item.get('description', ''),
                'img': item.get('img'),
                'origem': origem,
                'devotacao_descricao': item.get('details', {}).get('description', ''),
                'obrigacoes': [use['description'] for use in item.get('details', {}).get('uses', [])],
                'referencia_fonte': item.get('details', {}).get('reference', {}).get('source', ''),
                'referencia_pagina': item.get('details', {}).get('reference', {}).get('page', '')
            }
        )