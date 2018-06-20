from django.core.management.base import BaseCommand
from mediumparser.models import Tags, Store
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):

    BASE_URL = 'https://medium.com/search?q='
    BASE_ID = 1

    @staticmethod
    def get_article_db(link, url, tags_id):
        text = ""
        responses = requests.get(link)
        soup = BeautifulSoup(responses.content, 'html.parser')
        title = soup.select('.graf--title')[0].get_text()
        for link in soup.select('div.section-inner'):
            text += link.get_text()
        for link in soup.select('ul.tags a.link'):
            tag = link.get_text()
            Tags.objects.get_or_create(tags_id=tags_id,tags=tag)
        Store.objects.get_or_create(url=url, title=title, text=text, tags_id=tags_id)

    @staticmethod 
    def search_links_db(key, tags_id):
        response = requests.get(Command.BASE_URL + key)
        sp = BeautifulSoup(response.content, 'html.parser')
        for link in sp.select('div.postArticle-content a[data-action=open-post]'):
            url = link.get('href')
            Command.get_article_db(link.get('href'), url, tags_id)
            tags_id += 1

    @staticmethod 
    def seach_content(keys, tags_id):
        for key in keys:
            Command.search_links_db(key, tags_id)
            tags_id += 10

    def handle(self, *args, **options):
        with open("keys.txt") as file:
            keys = [row.strip() for row in file]
        Command.seach_content(keys, Command.BASE_ID)
