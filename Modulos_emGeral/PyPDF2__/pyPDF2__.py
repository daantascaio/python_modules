# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

FILE_RAIZ = Path(__file__).parent
FILE_ORIGIN_PDF = FILE_RAIZ / 'pdfs_origin'
NEW_DIR = FILE_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = FILE_ORIGIN_PDF / 'R20230210.pdf'
NEW_DIR.mkdir(exist_ok=True)


reader = PdfReader(RELATORIO_BACEN)

# print(reader.pages)
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]

# print(page0.extract_text())
print(page0.images[0])
imagem0 = page0.images[0]

with open(NEW_DIR / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_DIR / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore

files = [
    NEW_DIR / 'page1.pdf',
    NEW_DIR / 'page0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(NEW_DIR / 'MERGED.pdf')  # type: ignore
merger.close()
