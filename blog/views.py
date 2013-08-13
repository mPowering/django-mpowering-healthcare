from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext
from blog.models import Article


def index(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]
    latest_news_post = list_of_news.pop(0)

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'latest_news': latest_news_post,
        'list_news': list_of_news,
    })
    return render(request, 'blog/index.html', context)

def media_list():
    """ Retrieve list of blog posts """
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
        if news_item.can_comment == False:
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

""" view function for each page """
def task_forces(request, blog_id):
    pass

def partners(request):
    pass

def news_media(request, blog_id):
    """ View the News & Media page/tabe """
    pass

def resources(request, news_id):
    pass