# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

path_ = os.path.join('\\Users', 'caiod', 'Desktop', 'python_modules')

counter_ = count()

for root, dirs, files in os.walk(path_):
    if len(files) > 20:
        break 
    counter__ = next(counter_)
    print(counter__)
    print(f'ROOT: {root}')

    for dir_ in dirs:
        print(f'{counter__} | DIR: {dirs}')
    
        for files_ in files:
            print(f'{counter__} | FILES: {files}')
            # da pra fazer várias coisas, renomear, mudar, deletar e etc
            # os.unlink(files) isso é um delete, não execute 

