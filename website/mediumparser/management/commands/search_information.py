from django.core.management.base import BaseCommand
from mediumparser.models import Tag, Article
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):

    BASE_URL = 'https://medium.com/search?q='

    @staticmethod
    def store_article(link, url):
        text = ""
        responses = requests.get(link)
        soup = BeautifulSoup(responses.content, 'html.parser')
        title = soup.select('.graf--title')[0].get_text()
        for link in soup.select('div.section-inner'):
            text += link.get_text()
        article, _ = Article.objects.get_or_create(url=url, title=title, text=text)
        for link in soup.select('ul.tags a.link'):
            tag = link.get_text()
            tag, _ = Tag.objects.get_or_create(name=tag)
            article.tags.add(tag)

    @staticmethod 
    def search_links_db(key):
        response = requests.get(Command.BASE_URL + key)
        sp = BeautifulSoup(response.content, 'html.parser')
        for link in sp.select('div.postArticle-content a[data-action=open-post]'):
            url = link.get('href')
            Command.store_article(link.get('href'), url)


    @staticmethod 
    def seach_content(keys):
        for key in keys:
            Command.search_links_db(key)


    def handle(self, *args, **options):
        with open("keys.txt") as file:
            keys = [row.strip() for row in file]
        Command.seach_content(keys)
