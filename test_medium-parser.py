import pytest
import os
import requests

from main import search_links_db, get_article_db
from models import Store, Tags

class TestMediumParser:
	def test_type_error(self):
		with pytest.raises(TypeError):
			search_links_db("https://medium.com/search?q=Python")

	def test_check_correct_key_Python(self):
		with open("keys.txt") as file:
			keys = [row.strip() for row in file]
		assert keys[0] == "Python"

	def test_isfile(self):
		assert os.path.isfile('keys.txt') == True

	def test_type_check(self):
		with pytest.raises(TypeError):
			get_article_db("https://www.youtube.com/", "https://www.youtube.com/")

	def test_request(self):
		responses = requests.get("https://medium.com/")
		assert responses.status_code == 200

	def test_check_title(self):
		store = Store.get(Store.id == 1)
		assert store.title == "Learning Python: From Zero to Hero"

	def test_check_tag(self):
		tag = Tags.get(Tags.id == 1)
		assert tag.tags == "Python"

	def test_correct_tags(self):
		store = Store.get(Store.id == 1)
		assert store.tags == "Python|Programming|Coding|Web Development|Software Development|"

	def test_check_correct_key_Java(self):
		with open("keys.txt") as file:
			keys = [row.strip() for row in file]
		assert keys[1] == "Java"

	def test_extension(self):
		extension = ".txt"
		filename, file_extension = os.path.splitext('keys.txt')
		assert file_extension == extension

	def test_check_correct_key_Machine_Learning(self):
		with open("keys.txt") as file:
			keys = [row.strip() for row in file]
		assert keys[2] == "Machine Learning"
