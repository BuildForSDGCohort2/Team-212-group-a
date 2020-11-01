from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article


class ArticleAdmin(SummernoteModelAdmin):
    exclude = ('slug',)
    list_display = ('id', 'title', 'crop', 'stage', 'created_at')
    list_display_links = ('id', 'title')
    seach_fields = "title"
    list_per_page = 10
    summernote_fields = ("content")


admin.site.register(Article, ArticleAdmin)
