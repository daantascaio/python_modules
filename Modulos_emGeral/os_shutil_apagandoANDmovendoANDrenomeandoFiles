# # # # import os
# # # # import shutil 
# # # # # Usando expeanduser('~') para trabalhar na HOME do usuário
# # # # HOME = os.path.expanduser('~') 
# # # # # Unindo o caminho do HOME com o diretory 'Desktop'. OBS: Desktop pode mudar de
# # # # # nome, depende do OS do user.
# # # # DESKTOP = os.path.join(HOME, 'Desktop')
# # # # PASTA_ORIGINAL = os.path.join(DESKTOP, 'file_testing')
# # # # NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
# # # # print(HOME, DESKTOP, PASTA_ORIGINAL, NOVA_PASTA)
# # # # os.makedirs(NOVA_PASTA, exist_ok=True)
# # # # for root, dirs, files in os.walk(PASTA_ORIGINAL):
# # # #     for dir_ in dirs:
# # # #         caminnho_novo_diretorio = os.path.join(
# # # #             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
# # # #         )
# # # #         os.makedirs(caminnho_novo_diretorio, exist_ok=True)
# # # #     for file in files:
# # # #         caminho_arquivo = os.path.join(root, file)
# # # #         caminnho_novo_arquivo = os.path.join(
# # # #             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
# # # #         )
# # # #         shutil.copy(caminho_arquivo, caminnho_novo_arquivo)


"""
os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
Copiar Árvore recursivamente -> shutil.copytree
Apagar Árvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear/Mover -> shutil.move ou os.rename
"""
import os
import shutil

HOME = os.path.expanduser('~') 
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'file_testing')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# Usando o copytree para criar e copiar os arquviso dentro da pasta 'file_testing
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)

# Apaga a pasta para sempre, sem voltar nenhum erro
shutil.rmtree(NOVA_PASTA)

# Recriando a pasta apagada
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)

# Renomeando a pasta 'NOVA_PASTA' para 'NOVA_PASTA_EITA'
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

