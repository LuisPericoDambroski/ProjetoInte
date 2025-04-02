import json
from pathlib import Path
import sys

def corrigir_json(arquivo_entrada, pasta_json='../data/json-t20'):
    """Corrige caracteres problemáticos em um arquivo JSON"""
    try:
        # Caminho completo do arquivo
        caminho_entrada = Path(__file__).parent / pasta_json / arquivo_entrada
        
        if not caminho_entrada.exists():
            print(f"Erro: Arquivo {caminho_entrada} não encontrado!")
            return

        # Carrega o arquivo original
        with open(caminho_entrada, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Função para sanitizar strings
        def sanitizar(texto):
            if isinstance(texto, str):
                return texto.replace('`', "'").replace('´', "'")
            return texto
        
        # Processa os dados
        if isinstance(dados, list):
            for item in dados:
                for chave, valor in item.items():
                    item[chave] = sanitizar(valor)
        elif isinstance(dados, dict):
            for chave, valor in dados.items():
                dados[chave] = sanitizar(valor)
        
        # Salva o arquivo corrigido (sobrescreve o original)
        with open(caminho_entrada, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
            
        print(f"Arquivo {arquivo_entrada} corrigido com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar {arquivo_entrada}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python corrigir_jsons.py arquivo1.json [arquivo2.json ...]")
        print("Os arquivos devem estar em ../data/json-t20")
        sys.exit(1)
        
    for arquivo in sys.argv[1:]:
        corrigir_json(arquivo)