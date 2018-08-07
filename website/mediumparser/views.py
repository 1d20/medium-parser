import json

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import Article
from .filters import ArticleFilter, TagsFilter
from .forms import ArticleForm, UsersRegisterForm
from django.http import HttpResponse, JsonResponse

from rest_framework import generics, viewsets, decorators
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ArticleSerializer


User = get_user_model()    

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
    return render(request, "mediumparser/article_user_id.html", {'pk': id})
    # instance = get_object_or_404(Article, id=id)
    # form = ArticleForm(request.POST or None, instance=instance)
    # if form.is_valid():
    #     form.save()
    #     return redirect(art_name, id)

    # context = {
    #     "article": Article.objects.get(id=id),
    #     "form": form,
    # }
    # return render(request, "mediumparser/article_user_id.html", context)

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

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @decorators.list_route(["GET"])
    def my_route(self, request):
        # http://127.0.0.1:8000/articles/my_route/
        return Response({'key': 'val'})

    @decorators.detail_route(["GET"])
    def title(self, request, pk):
        # http://127.0.0.1:8000/articles/2/title/
        obj = self.get_object()
        return Response({'key': obj.title})
