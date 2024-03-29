from django.shortcuts import render, get_object_or_404
# from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core import serializers

from blog.forms import ContactForm
from blog.models import PressRelease, PressReleaseLink, Blog, Report, Presentation, Video, MapMarker

import distutils.core


def index(request):
    # list of news articles
    context = {
        'list_blogs': Blog.get_latest_blogs()[:5],
        'list_news': PressRelease.get_latest_news()[:4],
        'view_index': True,
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
    # check if any form data that needs to be emailed
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Member Sign up'
            message = ("Name: " +
                       form.cleaned_data['name'] +
                       ", Organization: " +
                       form.cleaned_data['organization'] +
                       ", Email: " +
                       form.cleaned_data['email'])

            sender = settings.EMAIL_FROM
            recipient = [form.cleaned_data['email']]

            send_mail(subject, message, sender, recipient)

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('blog:thanks'))
    else:
        form = ContactForm()

    context = {
        'active_page': "contact",
        'form': form,
    }

    return render(request,
                  'blog/contact.html',
                  context)

def thanks(request):
    context = {'active_page': "contact"}
    return render(request,
                  'blog/thanks.html',
                  context)

def test(request):
    return render(request,
                  'blog/test.html',
                  {'active_page': "objectives"})


def blog(request):
    """ Using paginator to view list of blog posts """
    # list of all blog entries
    blog_list_all = Blog.get_latest_blogs()
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
        'list_blogs': Blog.get_latest_blogs()[:5],
        'view_index': False,
        'main_list': blogs,
        'active_page': "blog",
    }
    return render(request, 'blog/blog.html',
                  context)


def blog_detail(request, blog_id, slug):
    # retrieve blog of interest
    article_of_interest = get_object_or_404(Blog, pk=blog_id)

    context = {
        'current_blog': article_of_interest,
        'list_blogs': Blog.get_latest_blogs()[:5],
        'view_index': False,
        'view_blog_entry': True,
        'active_page': "blog",
    }
    return render(request,
                  'blog/blog-detailed.html',
                  context)


def news_media_detail(request, blog_id, slug):
    # retrieve press release of interest
    article_of_interest = get_object_or_404(PressRelease, pk=blog_id)

    context = {
        'current_blog': article_of_interest,
        'list_news': PressRelease.get_latest_news()[:4],
        'view_index': False,
        'view_blog_entry': False,
        'active_page': "resources",
    }
    return render(request,
                  'blog/blog-detailed.html',
                  context)


def resources(request):
    # list of resources articles
    context = {
        'list_news_links': PressReleaseLink.get_latest_news()[:2],
        'list_news': PressRelease.get_latest_news()[:2],
        'list_reports': Report.get_latest_reports()[:4],
        'list_videos': Video.get_latest_videos()[:1],
        'view_index': False,
        'active_page': "resources",
    }
    return render(request, 'blog/resources.html',
                  context)


def resources_press_releases(request):
    articles_list_all = PressRelease.get_latest_news()

    paginator = Paginator(articles_list_all, 5)  # show 5 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        articles = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        articles = paginator.page(paginator.num_pages)

    context = {
        'view_index': False,
        'main_list': articles,
        'active_page': "resources",
    }

    return render(request, 'blog/resources_press_releases.html',
                  context)


def resources_external_links(request):
    articles_list_all = PressReleaseLink.get_latest_news()

    paginator = Paginator(articles_list_all, 5)  # show 5 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        articles = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        articles = paginator.page(paginator.num_pages)

    context = {
        'view_index': False,
        'main_list': articles,
        'active_page': "resources",
    }

    return render(request, 'blog/resources_external_links.html',
                  context)


def resources_reports_documents(request):
    # list of reports and docs

    # setup pager for reports
    reports_list_all = Report.get_latest_reports()
    paginator_reports = Paginator(reports_list_all, 4)  # show 4 articles/page
    page = request.GET.get('page')
    try:
        reports = paginator_reports.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        reports = paginator_reports.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        reports = paginator_reports.page(paginator_reports.num_pages)

    # setup pager for presenations
    present_list_all = Presentation.get_latest_presenations()
    paginator_present = Paginator(present_list_all, 5)  # show 5 articles/page
    page1 = request.GET.get('page')
    try:
        presentations = paginator_present.page(page1)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        presentations = paginator_present.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        presentations = paginator_present.page(paginator_present.num_pages)

    context = {
        'report_list': reports,
        'present_list': presentations,
        'view_index': False,
        'active_page': "resources",
    }
    return render(request, 'blog/resources_reports_documents.html',
                  context)


def resources_videos(request):
    # list of videos
    videos_list_all = Video.get_latest_videos()

    paginator = Paginator(videos_list_all, 5)  # show 5 articles per page
    page = request.GET.get('page')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        videos = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        videos = paginator.page(paginator.num_pages)

    context = {
        'main_list': videos,
        'view_index': False,
        'active_page': "resources",
    }
    return render(request, 'blog/resources_videos.html',
                  context)


def resources_calendar(request):
    # displays Google calendar
    context = {
        'view_index': False,
        'active_page': "resources",
        'calendar_id': settings.CALENDER_TOKEN,
    }
    return render(request, 'blog/resources_calendar.html',
                  context)


def resources_map(request):
    # displays map with loaded markers
    context = {
        'view_index': False,
        'active_page': "resources",
        'markers_list': serializers.serialize("json",
                                              MapMarker.get_latest_markers()),
        'map_id': settings.MAP_ID,
    }
    return render(request, 'blog/resources_map.html',
                  context)
