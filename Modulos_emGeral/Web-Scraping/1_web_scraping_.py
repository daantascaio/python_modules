# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import os
import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup

PATH_RAW_HTML_TXT = Path(__file__).parent / 'print-raw_html.txt'

url_ = 'http://127.0.0.1:3333/'
response = requests.get(url_)
raw_html = response.text  # the code retorn all HTML, view to file "print-raw_html.txt"
parsed_html = BeautifulSoup(raw_html, 'html.parser')

"""with open(PATH_RAW_HTML_TXT, 'w', encoding="utf8") as file:
    file.write(raw_html)"""

# if parsed_html is not None:
#     print(parsed_html.title)  # print = <title>Site</title>
# if parsed_html is not None:
#     print(parsed_html.title.text)  # print = Site

top_jobs_heading = parsed_html.select_one(
    '#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')
print(top_jobs_heading)  # print = <h2>TOP 3 jobs</h2>

if top_jobs_heading is not None:
    artcle = top_jobs_heading.parent

    if artcle is not None:
        for p in artcle.select('p'):
            print(re.sub(r'\s{2,}', '', p.text))
