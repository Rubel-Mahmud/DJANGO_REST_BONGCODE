from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):

    class Meta:
        model = Article
        fields = ('author', 'title', 'date_created')

admin.site.register(Article, ArticleAdmin)
