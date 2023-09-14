# We use pathlib to work with paths, folders and files so that one code works on Windows, Linux and Mac

from pathlib import Path

caminho_projeto = Path()
print(f'1 {caminho_projeto}')
print(f'2 {caminho_projeto.absolute()}')

caminho_projeto = Path(__file__)
print(f'3 {caminho_projeto}')

print(f'4 {caminho_projeto.parent}')

# print(f'5 {caminho_projeto.parent.parent}')
# print(f'6 {caminho_projeto.parent.parent.parent}')

criar_caminho = caminho_projeto.parent / 'criar_caminho'
print(f'7 {criar_caminho}')

criar_caminho = caminho_projeto.parent / 'criar_caminho' / 'arquivo.txt'
print(f'8 {criar_caminho}')
print()
print()

# arquivo = Path(__file__).parent / 'arquivo.txt'
# print(f'9 {Path.home()}')
# print(f"10 {Path.home() / 'Desktop'}")

# arquivo.touch() # Quando executado, será criado o meu 'arquivo.txt'

# arquivo.write_text('Hello World')
# print(arquivo.read_text())

# arquivo.unlink() # Apaga o meu 'arquivo.txt'

path_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
path_arquivo.touch()

with path_arquivo.open('a') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(path_arquivo.read_text())


PATH_FILE = Path(__file__).parent / 'pathlib_2.py'
PATH_FILE.touch()


