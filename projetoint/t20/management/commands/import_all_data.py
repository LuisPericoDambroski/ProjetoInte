import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from t20.models import *

class Command(BaseCommand):
    help = 'Importa TODOS os dados dos JSONs para os modelos Django'

    def handle(self, *args, **options):
        base_dir = Path('data')
        sources = {
            'json-t20': 'T20',
            'json-ghanor': 'Ghanor',
            'json-ameacas-arton': 'Ameacas',
            'json-deuses-e-herois': 'Deuses'
        }

        for source_dir, origem in sources.items():
            self.stdout.write(self.style.SUCCESS(f'Processando {source_dir}...'))
            self.process_source(base_dir / source_dir, origem)

    def process_source(self, source_dir, origem):
        processors = {
            # Acessórios
            'acessorios.json': self.process_acessorios,
            'accessories.json': self.process_acessorios,
            
            # Armaduras
            'armaduras.json': self.process_armaduras,
            'armaduras-random.json': self.process_armaduras_random,
            
            # Armas
            'armas.json': self.process_armas,
            'armas-random.json': self.process_armas_random,
            'armas-habilidades.json': self.process_habilidades_arma,
            
            # Itens Gerais
            'itens-gerais.json': self.process_itens_gerais,
            'alimentacao.json': self.process_alimentacao,
            'ferramentas.json': self.process_ferramentas,
            'veiculos.json': self.process_veiculos,
            'animais.json': self.process_animais,
            
            # Esotéricos e Alquímicos
            'esotericos.json': self.process_esotericos,
            'esotericos-random.json': self.process_esotericos_random,
            'alquimicos-preparados.json': self.process_alquimicos_preparados,
            'alquimicos-catalisadores.json': self.process_alquimicos_catalisadores,
            'alquimicos-venenos.json': self.process_alquimicos_venenos,
            
            # Magias e Poderes
            'magias.json': self.process_magias,
            'magias-custos.json': self.process_magias_custos,
            'poderes.json': self.process_poderes,
            
            # Melhorias e Encantos
            'melhorias.json': self.process_melhorias,
            'melhorias-random.json': self.process_melhorias_random,
            'melhorias-precos.json': self.process_melhorias_precos,
            'encantos-armaduras.json': self.process_encantos_armaduras,
            'encantos-armas.json': self.process_encantos_armas,
            'encantos-precos.json': self.process_encantos_precos,
            
            # Materiais Especiais
            'materiais-especiais.json': self.process_materiais_especiais,
            'materiais-especiais-precos.json': self.process_materiais_precos,
            
            # Condições e Perigos
            'condicoes.json': self.process_condicoes,
            'armadilhas.json': self.process_armadilhas,
            'doencas.json': self.process_doencas,
            'climas.json': self.process_climas,
            
            # Criaturas
            'estatisticas_criaturas_solo.json': lambda d, o: self.process_criaturas(d, o, 'solo'),
            'estatisticas_criaturas_lacaios.json': lambda d, o: self.process_criaturas(d, o, 'lacaio'),
            'estatisticas_criaturas_especiais.json': lambda d, o: self.process_criaturas(d, o, 'especial'),
            
            # Personagem
            'aparencias.json': self.process_aparencias,
            'trejeitos.json': self.process_trejeitos,
            'pericias.json': self.process_pericias,
            'erros_criticos.json': self.process_erros_criticos
        }

        for filename, processor in processors.items():
            file_path = source_dir / filename
            if not file_path.exists():
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]

                with transaction.atomic():
                    success = 0
                    for item in data:
                        try:
                            processor(item, origem)
                            success += 1
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(
                                f'Erro no item {item.get("nome")} de {filename}: {str(e)}'
                            ))

                    self.stdout.write(self.style.SUCCESS(
                        f'{filename}: {success}/{len(data)} itens importados'
                    ))

    # ========== PROCESSADORES ESPECÍFICOS ==========
    
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
                'bonus_defesa': item.get('bonus_defesa', 0),
                'penalidade': item.get('penalidade', 0),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso'),
                'slots': item.get('slots', 1),
                'modificadores': item.get('modificadores', {})
            }
        )

    def process_armas(self, item, origem):
        arma, created = Arma.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'classe': item.get('classe', 'simples'),
                'tipo': item.get('tipo', 'corte'),
                'empunhadura': item.get('empunhadura', 'uma_mao'),
                'dano': item['dano'],
                'critico': item.get('critico', 'x2'),
                'alcance': item.get('alcance'),
                'preco': item.get('preco', 0),
                'descricao': item.get('descricao', ''),
                'origem': origem,
                'peso': item.get('peso')
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

    def process_armas_random(self, item, origem):
        # Implementação similar à process_armas, com campos específicos para itens randômicos
        pass

    # ... (implementar TODOS os outros processadores seguindo o mesmo padrão)

    def process_magias(self, item, origem):
        Magia.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'descricao': item['descricao'],
                'escola': item['escola'],
                'circulo': item['circulo'],
                'componentes': item.get('componentes', ''),
                'alcance': item.get('alcance', ''),
                'duracao': item.get('duracao', ''),
                'aprimoramentos': item.get('aprimoramentos', [])
            }
        )

    def process_criaturas(self, item, origem, tipo):
        criatura, created = Criatura.objects.update_or_create(
            nome=item['nome'],
            defaults={
                'tipo': tipo,
                'nivel': item['nd'],
                'atributos': {
                    'FOR': item.get('forca'),
                    'DES': item.get('destreza'),
                    'CON': item.get('constituicao'),
                    'INT': item.get('inteligencia'),
                    'SAB': item.get('sabedoria'),
                    'CAR': item.get('carisma')
                },
                'tesouro': item.get('tesouro', {})
            }
        )
        
        if 'habilidades' in item:
            habilidades = []
            for hab in item['habilidades']:
                hab_obj, _ = HabilidadeCriatura.objects.get_or_create(
                    nome=hab['nome'],
                    defaults={
                        'descricao': hab.get('descricao', ''),
                        'tipo': hab.get('tipo', 'especial')
                    }
                )
                habilidades.append(hab_obj)
            criatura.habilidades.set(habilidades)

    # ... (implementar processadores para todos os outros tipos de dados)
