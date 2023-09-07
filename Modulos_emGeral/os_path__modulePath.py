# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.

# os.path.split: divide um caminho em uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').

# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

"""CAMINHO = os.path.join(r'Desktop', r'python_module', r'python.py')
print(CAMINHO)
print()

print(os.path.split(CAMINHO))
print()

repository, file = os.path.split(CAMINHO)
print(repository, file)
                                                        need refactoryng, error detected
name_file, ext_file = os.path.splitext(file)
print(name_file, ext_file)

print(os.path.exists(r'C:\\Users\\caio.dantas'))
print(os.path.abspath(r'.'))
print(os.path.abspath(r'locale_traducoes.py'))
print()
print(os.path.basename(CAMINHO))
print(os.path.basename(repository))"""

