import os
"""
from pathlib import Path

***
# CÓDIGO CRIADO APENAS PARA FORNECER OS ARQUIVOS A SEREM MANIPULADOS NESSA AULA
***

# Obtém o diretório do arquivo em execução
PATH_FILE = Path(__file__).parent.parent

# Nome das pastas que você deseja criar
pasta = ['file_testing']
 
# Loop para criar as pastas
for pasta in pasta:
    os.makedirs(PATH_FILE / pasta, exist_ok=True)  # exist_ok=True evita erros se a pasta já existir

# Define o caminho da pasta 'file_testing' em PATH_PASTA
PATH_PASTA = PATH_FILE / 'file_testing'

# Loop para criar arquivos TXT dentro da pasta 'file_testing'
for i in range(1, 6):
    nome_arquivo = f"arquivo{i}.txt"
    with open(PATH_PASTA / nome_arquivo, 'w') as arquivo:
        arquivo.write("Este é um arquivo de exemplo.")
        # Você pode adicionar conteúdo ao arquivo aqui, se desejar
"""

# os + shutil - Copiando arquivos com Python
# 1 - Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy

import shutil 

# Usando expeanduser('~') para trabalhar na HOME do usuário
HOME = os.path.expanduser('~') 

# Unindo o caminho do HOME com o diretory 'Desktop'. OBS: Desktop pode mudar de
# nome, depende do OS do user.
DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'file_testing')
print(HOME, DESKTOP, PASTA_ORIGINAL)
