# urls set here for blog app
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>\d+)/details$', views.details, name='details'),
    url(r'^task-forces/$', views.task_forces, name='task-forces'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^news-media/$', views.news_media, name='news-media'),
    url(r'^(?P<blog_id>\d+)/news-media$', views.news_media_detail, name='news-media_detail'),
    url(r'^resources/$', views.resources, name='resources'),
)
