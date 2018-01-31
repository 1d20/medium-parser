import requests
from bs4 import BeautifulSoup

def search_links (links):
	for links in soup.select('div.postArticle-content a[data-action=open-post]'):
		import requests
from bs4 import BeautifulSoup

def search_links (links):
	for links in soup.select('div.postArticle-content a[data-action=open-post]'):
		a =(links.get('href'))
		responses = requests.get(a)
		soup1 = BeautifulSoup(responses.content, 'html.parser')
		for links in soup1.select('div.section-inner'):
			print(links.get_text())
		for links in soup1.select('ul.tags a.link'):
			print(links.get_text())
			print(links.get('href'))

BASE_URL = 'https://medium.com/search?q=Python'

response = requests.get(BASE_URL)

soup = BeautifulSoup(response.content, 'html.parser')

search_links(soup)

