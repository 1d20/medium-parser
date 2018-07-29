from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'article_update/<id>', views.article_update, name='article_update'),
    path(r'article/<id>', views.art_name, name='art_name'),
    url(r'^profile$', views.profile, name='profile'),
    path(r'profile/<id>', views.profile_id, name='profile_id'),
    path(r'profile_update/<id>', views.profile_update, name='profile_update'),
]
