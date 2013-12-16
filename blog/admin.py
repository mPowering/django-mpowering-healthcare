from django.contrib import admin
from blog.models import Article, Report, Presentation, Video
from blog.forms import ArticleModelAdminForm, ReportModelAdminForm, PresentationModelAdminForm, VideoModelAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently', 'can_comment')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleModelAdminForm

admin.site.register(Article, ArticleAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = ReportModelAdminForm

admin.site.register(Report, ReportAdmin)


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = PresentationModelAdminForm

admin.site.register(Presentation, PresentationAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = VideoModelAdminForm

admin.site.register(Video, VideoAdmin)

