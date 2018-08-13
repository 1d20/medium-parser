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

def profile(request):
    if request.user.is_authenticated:
        return render(request, "mediumparser/profile.html", {"articles": Article.objects.filter(author_id=request.user.id)})
    else: 
        return HttpResponseRedirect("/login")

def profile_id(request, id):
    return render(request, "mediumparser/profile_id.html", {'pk': id})

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
