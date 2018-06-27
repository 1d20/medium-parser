from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    context = {"articles": Article.objects.all()}
    return render(request, "mediumparser/index.html", context)

def article_new(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.url = None
        article.save()
    else:
        print(form.errors)
    return redirect(index)

def article(request, id):
    context = {"article": Article.objects.get(id=id)}
    return render(request, "mediumparser/article.html", context)
