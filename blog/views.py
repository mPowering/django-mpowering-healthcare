from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext
from blog.models import Article


def index(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]
    print len(list_of_news)

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': True,
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

""" view function for each page/tab """
def task_forces(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
    })
    return render(request, 'blog/task-forces.html', context)

def partners(request):
    return render(request, 'blog/partners.html')

def news_media(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
    })
    return render(request, 'blog/blog.html', context)

def news_media_detail(request, blog_id):
    # retrieve blog of interest
    blog = get_object_or_404(Article, pk=blog_id)

    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'blog_title': blog.title,
        'blog_date': blog.pub_date,
        'blog_body': blog.body,

        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
    })
    return render(request, 'blog/blog-detailed.html', context)

def resources(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
    })
    return render(request, 'blog/media-release.html', context)