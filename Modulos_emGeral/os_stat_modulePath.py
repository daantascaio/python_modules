# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

# print(formata_tamanho(10))
# print(formata_tamanho(100))
# print(formata_tamanho(1000))
# print(formata_tamanho(10000))
# print(formata_tamanho(100000))
# print(formata_tamanho(1000000))
# print(formata_tamanho(10000000))
# print(formata_tamanho(100000000))
# print(formata_tamanho(1000000000))
# print(formata_tamanho(10000000000))


path_ = os.path.join('\\Users', 'caiod', 'Desktop', 'python_modules')

counter_ = count()

for root, dirs, files in os.walk(path_):

    counter = next(counter_)
    if counter > 100:
        raise

    print(counter, 'ROOT:', root)

    for dir_ in dirs:
        print(' ', counter, 'DIR:', dir_)

        for file_ in files:
            path_ = os.path.join(root, file_)
            stats = os.stat(path_)
            tamanho = stats.st_size
            print(' ', counter, 'FILE:', file_, formata_tamanho(tamanho))
