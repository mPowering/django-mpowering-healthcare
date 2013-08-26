from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article


def index(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': True,
    })
    return render(request, 'blog/index.html', context)


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


""" Using paginator to view list of blog posts """
def news_media(request):
    # list of all blog entries
    blog_list_all = get_list_or_404(Article)
    paginator = Paginator(blog_list_all, 5) # show 5 blogs per page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        blogs = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        blogs = paginator.page(paginator.num_pages)

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
        'main_list': blogs,
    })
    return render(request, 'blog/blog.html', context)


def news_media_detail(request, blog_id):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x:x.pub_date, reverse=True)[:5]
    
    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x:x.pub_date, reverse=True)[:4]

    # retrieve blog of interest
    blog = get_object_or_404(Article, pk=blog_id)

    # list latest blog entries
    print len(blog_list)
    if len(blog_list) > 0:
        for b in blog_list:
            if b == blog:
                blog_list.remove(b)
        latest_blog_post = blog_list.pop(0) # retrieve latest blog post

    context = RequestContext(request, {
        'current_blog': blog,

        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
        'view_blog_entry': blog.can_comment,
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


""" helper function """
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
