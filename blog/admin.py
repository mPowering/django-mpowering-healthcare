from django.contrib import admin
from blog.models import Article
from blog.forms import ArticleModelAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently', 'can_comment')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = ArticleModelAdminForm

admin.site.register(Article, ArticleAdmin)
