from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'article/<id>', views.art_name, name='art_name'),
    url(r'^profile$', views.profile, name='profile'),
    path(r'profile/<id>', views.profile_id, name='profile_id'),
    path(r'profile_update/<id>', views.profile_update, name='profile_update'),
    url(r'api/', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)

