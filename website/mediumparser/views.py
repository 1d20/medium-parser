import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import Article
from .filters import ArticleFilter
from .forms import ArticleForm, UsersRegisterForm

User = get_user_model()

def article_update(request, id):
    instance = get_object_or_404(Article, id=id)

    if len(request.POST.keys()) == 1:
        form = ArticleForm(instance=instance)
        return HttpResponse(json.dumps({'form': form.as_p()}), content_type="application/json")
    
    form = ArticleForm(request.POST, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps({'result': 'ok'}), content_type="application/json")
    
    return HttpResponse(
        json.dumps({'form': form.as_p()}),
        content_type="application/json",
        status=400
    )
    

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

def art_name(request, id):
    instance = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(art_name, id)

    context = {
        "article": Article.objects.get(id=id),
        "form": form,
    }
    return render(request, "mediumparser/article_user_id.html", context)

def profile(request):
    if request.user.is_authenticated:
        form = UsersRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get("password")	
            user.set_password(password)
            user.save()
            new_user = authenticate(username = user.username, password = password)
            login(request, new_user)
            return redirect("/login")
        context = {
                "articles": Article.objects.filter(author_id=request.user.id),
                "form" : form,
                }
        return render(request, "mediumparser/profile.html", context)
    else: 
        return HttpResponseRedirect("/login")

def profile_id(request, id):
    context = {
            "articles": Article.objects.filter(author_id=id),
            "author": User.objects.get(id=id),
            }
    return render(request, "mediumparser/profile_id.html", context)

def profile_update(request, id):
    instance = get_object_or_404(User, id=id)
    if len(request.POST.keys()) == 1:
        form = UsersRegisterForm(instance=instance)
        return HttpResponse(json.dumps({'form': form.as_p()}), content_type="application/json")
    
    form = UsersRegisterForm(request.POST, instance=instance)
    if form.is_valid():
        form.save()
        user = form.save()
        password = form.cleaned_data.get("password")	
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return HttpResponse(json.dumps({'result': 'ok'}), content_type="application/json")
    
    return HttpResponse(
        json.dumps({'form': form.as_p()}),
        content_type="application/json",
        status=400
    )
