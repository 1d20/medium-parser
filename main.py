# medium-parser

import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://medium.com/search?q=Python'


def get_article(link):
    responses = requests.get(link)
    soup = BeautifulSoup(responses.content, 'html.parser')
    information_one_headers = {'title': '', 'text': '', 'tags': []}
    information_one_headers['title'] = soup.select('.graf--title')[0].get_text()
    for link in soup.select('div.section-inner'):
        information_one_headers['text'] += link.get_text()
    for link in soup.select('ul.tags a.link'):
        information_one_headers['tags'].append(link.get_text())
    return information_one_headers


def search_links():
    response = requests.get(BASE_URL)
    sp = BeautifulSoup(response.content, 'html.parser')
    information = []
    for link in sp.select('div.postArticle-content a[data-action=open-post]'):
        information.append(get_article(link.get('href')))

    with open('Information.txt', 'w') as f_out:
        json.dump(information, f_out)

    with open('Information.txt', 'r') as f_in:
        a1 = json.load(f_in)
        print([a['title'] for a in a1])

search_links()
