from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Article
from .filters import ArticleFilter
from .forms import ArticleForm


def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = ArticleForm()

        context = {
            "articles": ArticleFilter(request.GET, queryset=Article.objects.all()),
            "form": form,
        }

    return render(request, "mediumparser/index.html", context)


def article(request, id):
    context = {"article": Article.objects.get(id=id)}
    return render(request, "mediumparser/article.html", context)


def art_name(request, id):
    context = {"article": Article.objects.get(id=id)}
    return render(request, "mediumparser/article_user_id.html", context)
