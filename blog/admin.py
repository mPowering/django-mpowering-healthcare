from django.contrib import admin
from blog.models import Article, Report, Presentation
from blog.forms import ArticleModelAdminForm, ReportModelAdminForm, PresentationModelAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently', 'can_comment')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = ArticleModelAdminForm

admin.site.register(Article, ArticleAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = ReportModelAdminForm

admin.site.register(Report, ReportAdmin)


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = PresentationModelAdminForm

admin.site.register(Presentation, PresentationAdmin)
