# urls set here for blog app
from django.conf.urls import patterns, url
from blog import views
from django.conf import settings


urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^task-forces/$', views.task_forces, name='task-forces'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^news-media/$', views.news_media, name='news-media'),
    url(r'^(?P<blog_id>\d+)/news-media-detail$', views.news_media_detail, name='news-media-detail'),
    url(r'^resources/$', views.resources, name='resources'),

    url(r'^media/(?P<path>.*)$', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT})
)
