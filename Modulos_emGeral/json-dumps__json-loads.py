# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
      title: str
      original_title: str
      is_movie: bool
      imdb_rating: float
      year: int
      characters: list[str]
      budget: None | float
# Str normal em python, usando ''' ''' porq caiu como uma luva para exemplificar 
# o object json
string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
  }
'''
# Convertendo para JSON
# filme = json.loads(string_json)
filme: Movie = json.loads(string_json)

# Usando pprint para ver o print de maneira mais elegante
# pprint(filme)
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year'] + 10)