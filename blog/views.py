from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import RequestContext
from blog.models import BlogMedia

def index(request):
    # list latest blog entries
    latest_blog_list = get_list_or_404(BlogMedia)
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
    })
    return render(request, 'blog/index.html', context)

def details(request, blog_id):
    # view individual blogs in more detail
    blog = get_object_or_404(BlogMedia, pk=blog_id)
    
    context = RequestContext(request, {
        'title': blog.title,
        'pub_date': blog.pub_date,
        'body': blog.body,
    })

    return render(request, 'blog/details.html', context)
