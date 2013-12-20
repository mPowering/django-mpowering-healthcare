# urls set here for blog app
from django.conf.urls import patterns, url
from blog import views
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^objectives/$', views.objectives, name='objectives'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<blog_id>\d+)/(?P<slug>[\w-]+)/$', views.blog_detail, name='blog-detail'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^resources/(?P<blog_id>\d+)/news-media-detail/(?P<slug>[\w-]+)/$', views.news_media_detail, name='news-media-detail'),
    url(r'^resources/news_articles/$', views.resources_news_articles, name='resources_news_articles'),
    url(r'^resources/news_articles/(?P<view_external_articles>\w+)/$', views.resources_news_articles_list_all, name='resources_news_articles_list_all'),
    url(r'^resources/reports/$', views.resources_reports_documents, name='resources_reports_documents'),
    url(r'^resources/videos/$', views.resources_videos, name='resources_videos'),
    url(r'^resources/map/$', views.resources_map, name='resources_map'),
    url(r'^resources/calendar/$', views.resources_calendar, name='resources_calendar'),
    url(r'^contact/$', views.contact, name='contact'),
    
    url(r'^media/(?P<path>.*)$', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT})
)
