from django.contrib import admin
from blog.models import NewsArticle, NewsArticleLink, Blog, Report, Presentation, Video
from blog.forms import NewsArticleModelAdminForm, ReportModelAdminForm, PresentationModelAdminForm, VideoModelAdminForm, NewsArticleLinkModelAdminForm, BlogModelAdminForm


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = NewsArticleModelAdminForm

admin.site.register(NewsArticle, NewsArticleAdmin)


class NewsArticleLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = NewsArticleLinkModelAdminForm

admin.site.register(NewsArticleLink, NewsArticleLinkAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = BlogModelAdminForm

admin.site.register(Blog, BlogAdmin)


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

