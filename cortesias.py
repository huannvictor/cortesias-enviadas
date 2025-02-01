import os
from collections import defaultdict
import pandas as pd

def listar_arquivos(caminho_pasta):
    # Lista todos os arquivos no diretório
    return [arquivo for arquivo in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, arquivo))]

def processar_arquivos(arquivos):
    # Estrutura de dados para armazenar as informações
    dados_escolas = defaultdict(lambda: {"ano": 2025, "paginas_solicitadas": set()})

    for arquivo in arquivos:
        # Remove a extensão .JPG e divide o nome do arquivo
        nome_sem_extensao = arquivo.split('.')[0]
        partes = nome_sem_extensao.split('_')

        if len(partes) == 3:  # Garante que o nome do arquivo está no formato esperado
            codigo_escola, ano, pagina = partes

            # Filtra apenas o ano de 2025
            if ano == "2025":
                # Adiciona a página ao conjunto de páginas da escola
                dados_escolas[codigo_escola]["paginas_solicitadas"].add(pagina)

    # Converte o conjunto de páginas para a quantidade de páginas
    for codigo_escola, info in dados_escolas.items():
        info["paginas_solicitadas"] = len(info["paginas_solicitadas"])

    return dados_escolas

def salvar_em_excel(dados_escolas, caminho_saida):
    # Converte o dicionário em um DataFrame do pandas
    dados = []
    for codigo_escola, info in dados_escolas.items():
        dados.append([codigo_escola, info["ano"], info["paginas_solicitadas"]])

    df = pd.DataFrame(dados, columns=["Código da Escola", "Ano", "Páginas Solicitadas"])

    # Salva o DataFrame em um arquivo Excel
    df.to_excel(caminho_saida, index=False)

# Caminho da pasta que você quer listar os arquivos
caminho_pasta = r'C:\Digitalizacao_Cortesias\Processadas'

# Caminho de saída para o arquivo Excel
caminho_saida = r'C:\Digitalizacao_Cortesias\relatorio_escolas_2025.xlsx'

# Lista os arquivos
arquivos = listar_arquivos(caminho_pasta)

# Processa os arquivos e gera a estrutura de dados
dados_escolas = processar_arquivos(arquivos)

# Salva os dados em uma planilha Excel
salvar_em_excel(dados_escolas, caminho_saida)

print(f"Relatório salvo em: {caminho_saida}")