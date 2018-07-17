from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # path(r'article/<id>', views.article, name='article'),
    path(r'article/<id>', views.art_name, name='art_name'),
]
