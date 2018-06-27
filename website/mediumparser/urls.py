from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('create', views.article_new, name='article_new'),
    path(r'article/<id>', views.article, name='article'),
]
