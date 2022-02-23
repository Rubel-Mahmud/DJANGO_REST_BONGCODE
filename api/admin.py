from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created', 'is_public')

admin.site.register(Article, ArticleAdmin)
