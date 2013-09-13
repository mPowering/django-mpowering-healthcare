from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from blog.models import Article


def index(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x: x.pub_date, reverse=True)[:5]
    latest_blog_post = None
    if len(blog_list) > 0:
        latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x: x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': True,
        'company': settings.COMPANY_NAME,
        'active_page': "index",
    })
    return render(request, 'blog/index.html', context)


def objectives(request):
    """ view function for each page/tab """
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x: x.pub_date, reverse=True)[:5]
    latest_blog_post = None
    if len(blog_list) > 0:
        latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x: x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "objectives",
    })
    return render(request, 'blog/objectives.html', context)


def partners(request):
    context = RequestContext(request, {
        'active_page': "partners",
        })
    return render(request, 'blog/partners.html', context)

def test(request):
    context = RequestContext(request, {
        'active_page': "objectives",
        })
    return render(request, 'blog/test.html', context)

def news_media(request):
    """ Using paginator to view list of blog posts """
    # list of all blog entries
    blog_list_all = Article.objects.all()
    paginator = Paginator(blog_list_all, 5)  # show 5 blogs per page
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
    blog_list = sorted(media_list(), key=lambda x: x.pub_date, reverse=True)

    # remove posts that will be displayed in the pager are not also displayed in the side menu
    for temp_blog_1 in blogs:
        for temp_blog_2 in blog_list:
            if temp_blog_1 == temp_blog_2:
                blog_list.remove(temp_blog_2)

    latest_blog_post = None
    if len(blog_list) > 0:
        latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x: x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
        'main_list': blogs,
        'company': settings.COMPANY_NAME,
        'active_page': "news_media",
    })
    return render(request, 'blog/blog.html', context)


def news_media_detail(request, blog_id):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x: x.pub_date, reverse=True)[:6]

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x: x.pub_date, reverse=True)[:5]

    # retrieve blog of interest
    article_of_interest = get_object_or_404(Article, pk=blog_id)

    # remove current article from short list
    if article_of_interest.can_comment:
        if len(blog_list) > 0:
            for b in blog_list:
                if b == article_of_interest:
                    blog_list.remove(b)
    else:
        if len(list_of_news) > 0:
            for b in list_of_news:
                if b == article_of_interest:
                    list_of_news.remove(b)

    list_of_news = list_of_news[:4]  # ensures only 4 news-posts visible in short list
    blog_list = blog_list[:5]  # ensures only 5 blog-posts visible in short list
    latest_blog_post = None
    if len(blog_list) > 0:
        latest_blog_post = blog_list.pop(0)  # retrieve latest blog post

    context = RequestContext(request, {
        'current_blog': article_of_interest,

        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
        'view_blog_entry': article_of_interest.can_comment,
        'company': settings.COMPANY_NAME,
        'active_page': "news_media",
    })
    return render(request, 'blog/blog-detailed.html', context)


def resources(request):
    # list latest blog entries
    blog_list = sorted(media_list(), key=lambda x: x.pub_date, reverse=True)[:5]
    latest_blog_post = None
    if len(blog_list) > 0:
        latest_blog_post = blog_list.pop(0)

    # list of news articles
    list_of_news = sorted(news_list(), key=lambda x: x.pub_date, reverse=True)[:4]

    context = RequestContext(request, {
        'latest_blog': latest_blog_post,
        'list_blogs': blog_list,
        'list_news': list_of_news,
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    })
    return render(request, 'blog/media-release.html', context)


""" helper function """


def media_list():
    """ Retrieve list of blog posts """
    list_all = Article.objects.all()
    blog_list = []
    for blog in list_all:
        if blog.can_comment:
            blog_list.append(blog)

    return blog_list


def news_list():
    """ Retrieve list of news articles """
    list_all = Article.objects.all()
    news_list = []
    for news_item in list_all:
        if not news_item.can_comment:
            news_list.append(news_item)

    return news_list
