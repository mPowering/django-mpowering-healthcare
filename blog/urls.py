# urls set here for blog app
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>\d+)/details$', views.details, name='details'),
    url(r'^(?P<blog_id>\d+)/task_forces$', views.task_forces, name='task_forces'),
    url(r'^/partners$', views.partners, name='partners'),
    url(r'^(?P<blog_id>\d+)/news_media$', views.news_media, name='news_media'),
    url(r'^(?P<news_id>\d+)/resources$', views.resources, name='resources'),
)
