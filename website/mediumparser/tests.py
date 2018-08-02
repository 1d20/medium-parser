from django.test import TestCase

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User

from . import views
from .forms import UsersRegisterForm
from accounts.forms import UsersLoginForm


class MyTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example', email='example@123.com')
        self.user.set_password('123')
        self.user.save()

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_form_register(self):
        form_data = { "username" : "hello",
            "email": "example@gmail.com",
            "confirm_email" : "example@gmail.com", 
            "password" : "12345678",
        }
        form = UsersRegisterForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
    
    def test_url(self):
        url = reverse('profile_update', args=[1])
        self.assertEqual(url, '/profile_update/1')

    def test_authenticate(self):
        self.assertTrue(self.user.is_authenticated)

    def test_form_login(self):
        form_data = { "username" : "example",
            "password" : "123",
        }
        form = UsersLoginForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
