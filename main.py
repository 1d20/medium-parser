# medium-parser

import requests
from bs4 import BeautifulSoup
from models import Store, Tags

BASE_URL = 'https://medium.com/search?q='
BASE_ID = 1

def get_article_db(link, url, tags_id):
    text = ""
    responses = requests.get(link)
    soup = BeautifulSoup(responses.content, 'html.parser')
    title = soup.select('.graf--title')[0].get_text()
    for link in soup.select('div.section-inner'):
        text += link.get_text()
    for link in soup.select('ul.tags a.link'):
        tag = link.get_text()
        Tags.get_or_create(tags_id=tags_id,tags=tag)
    Store.get_or_create(url=url, title=title, text=text, tags=tags_id)


def search_links_db(key, tags_id):
    response = requests.get(BASE_URL + key)
    sp = BeautifulSoup(response.content, 'html.parser')
    for link in sp.select('div.postArticle-content a[data-action=open-post]'):
        url = link.get('href')
        get_article_db(link.get('href'), url, tags_id)
        tags_id += 1

def seach_content(keys, tags_id):
    for key in keys:
        search_links_db(key, tags_id)
        tags_id += 10

with open("keys.txt") as file:
    keys = [row.strip() for row in file]

seach_content(keys, BASE_ID)
