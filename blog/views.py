from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext
from blog.models import Article

from django.views import generic
from django.core.urlresolvers import reverse

def index(request):
    # list latest blog entries
    latest_blog_list = media_list()
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
    })
    return render(request, 'blog/index.html', context)

class HomeView(generic.ListView):
    """ View landing page for news and media articles """
    pass

class NewsDetailView(generic.DetailView):
    """ View one detailed news article """
    pass

class MediaDetailView(generic.DetailView):
    """ View one detailed media article/blog """
    pass

def media_list():
    """ Retrieve list of blogs """
    list_all = get_list_or_404(Article)
    blog_list = []
    for blog in list_all:
        if blog.can_comment == True:
            blog_list.append(blog)

    return blog_list

def news_list():
    """ Retrieve list of news articles """
    list_all = get_list_or_404(Article)
    news_list = []
    for news_item in list_all:
        if news_item.can_comment == True:
            news_list.append(news_item)

    return news_list

def details(request, blog_id):
    # view individual blogs in more detail
    blog = get_object_or_404(Article, pk=blog_id)
    
    context = RequestContext(request, {
        'title': blog.title,
        'pub_date': blog.pub_date,
        'body': blog.body,
    })

    return render(request, 'blog/details.html', context)