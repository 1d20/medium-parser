from django.db import models
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def show_url(self):
        return format_html("<a href='{url}'>{url}</a>", url=self.url)
    show_url.short_description = 'url'

    def short_text(self):
        return truncatechars(self.text, 100)
    short_text.short_description = 'text'

      
