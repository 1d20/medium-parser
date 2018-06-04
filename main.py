# medium-parser

import requests
from bs4 import BeautifulSoup
from models import Store


def get_article_db(link, url):
    text = ""
    tags = ""
    responses = requests.get(link)
    soup = BeautifulSoup(responses.content, 'html.parser')
    title = soup.select('.graf--title')[0].get_text()
    for link in soup.select('div.section-inner'):
        text += link.get_text()
    for link in soup.select('ul.tags a.link'):
        tags += link.get_text() + "|"
    Store.get_or_create(url=url, title=title, tags=tags, text=text)


def search_links_db():
    response = requests.get(BASE_URL)
    sp = BeautifulSoup(response.content, 'html.parser')
    for link in sp.select('div.postArticle-content a[data-action=open-post]'):
        url = link.get('href')
        get_article_db(link.get('href'), url)


with open("keys.txt") as file:
    keys = [row.strip() for row in file]

for key in keys:
    BASE_URL = 'https://medium.com/search?q=' + key
    search_links_db()
