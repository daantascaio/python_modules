from pathlib import Path
from shutil import rmtree
# PATH_FILE = Path.home() / 'Desktop' / 'arquivo.txt'
# PATH_FILE.touch()
# PATH_FILE.write_text('Hello World!')

# PATH_FILE.unlink

PATH_FILE = Path.home() / 'Desktop' / 'Pasta'

PATH_FILE.mkdir(exist_ok=True)
SUBPASTA = PATH_FILE / 'SUBPASTA'
SUBPASTA.mkdir(exist_ok=True)

OTHER_FILE = SUBPASTA / 'arquivo.txt'
OTHER_FILE.touch()
OTHER_FILE.write_text('Hey')

OTHER_OTHER_FILE = PATH_FILE / 'arquivo.txt'
OTHER_OTHER_FILE.touch()
OTHER_OTHER_FILE.write_text('Hey')

FILES = PATH_FILE / 'files'
FILES.mkdir(exist_ok=True)

for i in range(10):
    file = FILES / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write(f'file_{i}.txt')
    
# rmtree(PATH_FILE)

def rmtree(root: Path, remove_root=True):

    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(PATH_FILE)

    