from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','short_text','show_url')
    list_filter = ['tags']


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
