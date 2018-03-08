# medium-parser

import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://medium.com/search?q=Python'


def search_links(links):
    information = []
    for links in sp.select('div.postArticle-content a[data-action=open-post]'):
        a = (links.get('href'))
        responses = requests.get(a)
        soup = BeautifulSoup(responses.content, 'html.parser')
        for links in soup.select('div.section-inner'):
            information.append(links.get_text())
        for links in soup.select('ul.tags a.link'):
            information.append(links.get_text())
            information.append(links.get('href'))

    with open('Information.txt', 'w') as f_out:
        json.dump(information, f_out)

response = requests.get(BASE_URL)

sp = BeautifulSoup(response.content, 'html.parser')

search_links(sp)
