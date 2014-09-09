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
    url(r'^resources/press_releases/$', views.resources_press_releases, name='resources_press_releases'),
    url(r'^resources/reports/$', views.resources_reports_documents, name='resources_reports_documents'),
    url(r'^resources/external_links/$', views.resources_external_links, name='resources_external_links'),
    url(r'^resources/videos/$', views.resources_videos, name='resources_videos'),
    url(r'^resources/map/$', views.resources_map, name='resources_map'),
    url(r'^resources/calendar/$', views.resources_calendar, name='resources_calendar'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),

    url(r'^media/(?P<path>.*)$', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT})
)
