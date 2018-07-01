from django import forms
from .models import Tag, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
