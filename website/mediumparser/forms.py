from django import forms
from .models import Tag, Article


class ArticleForm(forms.Form):
    # url = forms.URLField(max_length=50)
    title = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

