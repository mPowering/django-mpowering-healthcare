from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from blog.models import Article, Report


def index(request):
    # list of news articles
    context = {
        'list_blogs': Article.get_latest_blogs()[:5],
        'list_news': Article.get_latest_news()[:4],
        'view_index': True,
        'company': settings.COMPANY_NAME,
        'active_page': "index",
    }
    return render(request,
                  'blog/index.html',
                  context)


def objectives(request):
    """ view function for each page/tab """
    # list of news articles
    context = {
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "objectives",
    }
    return render(request,
                  'blog/objectives.html',
                   context)


def partners(request):
    context = {'active_page': "partners"}
    return render(request,
                  'blog/partners.html',
                  context)


def contact(request):
    return render(request,
                  'blog/contact.html',
                  {'active_page': "contact"})


def test(request):
    return render(request,
                  'blog/test.html',
                  {'active_page': "objectives"})


def blog(request):
    """ Using paginator to view list of blog posts """
    # list of all blog entries
    blog_list_all = Article.get_latest_blogs()
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

    context = {
        'list_blogs': Article.get_latest_blogs()[:5],
        'list_news': Article.get_latest_news()[:4],
        'view_index': False,
        'main_list': blogs,
        'company': settings.COMPANY_NAME,
        'active_page': "blog",
    }
    return render(request, 'blog/blog.html',
                  context)


def blog_detail(request, blog_id):
    # retrieve blog of interest
    article_of_interest = get_object_or_404(Article, pk=blog_id)

    context = {
        'current_blog': article_of_interest,
        'list_blogs': Article.get_latest_blogs()[:5],
        'list_news': Article.get_latest_news()[:4],
        'view_index': False,
        'view_blog_entry': article_of_interest.can_comment,
        'company': settings.COMPANY_NAME,
        'active_page': "blog",
    }
    return render(request,
                  'blog/blog-detailed.html',
                  context)


def news_media_detail(request, blog_id):
    # retrieve blog of interest
    article_of_interest = get_object_or_404(Article, pk=blog_id)

    context = {
        'current_blog': article_of_interest,
        'list_blogs': Article.get_latest_blogs()[:5],
        'list_news': Article.get_latest_news()[:4],
        'view_index': False,
        'view_blog_entry': article_of_interest.can_comment,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    }
    return render(request,
                  'blog/blog-detailed.html',
                  context)


def resources(request):
    # list of news articles
    context = {
        'list_news': Article.get_latest_news()[:4],
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    }
    return render(request, 'blog/resources.html',
                  context)


def resources_news_articles(request):
    # list of news articles
    context = {
        'list_news': Article.get_latest_news(),
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    }
    return render(request, 'blog/resources_news_articles.html',
                  context)


def resources_news_articles_list_all(request, view_external_articles):
    if view_external_articles=='True':
        view_external_articles = True
    else:
        view_external_articles = False

    # list of news articles
    context = {
        'list_news': Article.get_latest_news(),
        'view_index': False,
        'view_external_articles': view_external_articles,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    }
    return render(request, 'blog/resources_news_articles_list_all.html',
                  context)


def resources_reports_documents(request):
    # list of news articles
    context = {
        'list_reports': Report.get_latest_reports(),
        'view_index': False,
        'company': settings.COMPANY_NAME,
        'active_page': "resources",
    }
    return render(request, 'blog/resources_reports_documents.html',
                  context)
