from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
import django_filters

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ["tags"]


def index(request):
    filter = ArticleFilter(request.GET, queryset=Article.objects.all())
    context = {
        "articles": Article.objects.all(),
        'filter': filter,
        }
    return render(request, "mediumparser/index.html", context)

def article_new(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.url = None
        article.tags = None
        article.save()
    else:
        print(form.errors)
    return redirect(index)

def article(request, id):
    context = {"article": Article.objects.get(id=id)}
    return render(request, "mediumparser/article.html", context)

def art_name(request, id):
    context = {"article": Article.objects.get(id=id)}
    return render(request, "mediumparser/article_user_id.html", context)
