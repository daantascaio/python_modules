# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'file_1.csv' 

# Reading in -> list <- format using -> csv.reader
"""with open(PATH_CSV, 'r') as file_csv:
    reader_csv = csv.reader(file_csv)
    
    print('FORMAT READING -> list[str]')
    for line in reader_csv:
        # print(line)
        print(f'{line[1]} || {type(line[1])} ||  {type(line)}')"""

# Reading in -> dict <- format using -> csv.DictReader
with open(PATH_CSV, 'r') as file_csv:
    reader_csv = csv.DictReader(file_csv)
    
    print('FORMAT READING -> dict')
    for line in reader_csv:
        print(line['Nome'], line['Idade'], line['Endereco'])
        
    
    
        