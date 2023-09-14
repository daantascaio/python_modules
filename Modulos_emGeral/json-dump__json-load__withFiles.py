# json.dump and json.load with files
import json
import os

PATH_FILE = 'json-dump__json-load__withFiles.json'

# '.abspath' return a absolute path. Windows -> C: || Linux -> /
ABSOLUTE_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        PATH_FILE
    )
)

dict_movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(ABSOLUTE_FILE_PATH, 'w') as arquivo:
    json.dump(dict_movie, arquivo, ensure_ascii=False, indent=2)

with open(ABSOLUTE_FILE_PATH, 'r') as arquivo:
    movie_json = json.load(arquivo)
    print(movie_json)
