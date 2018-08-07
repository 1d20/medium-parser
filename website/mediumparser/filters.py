import django_filters

from .models import Article
from django_filters import rest_framework as filters


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ["tags"]

class TagsFilter(filters.FilterSet):
    class Meta:
        model = Article
        fields = ['tags']
