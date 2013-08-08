from django.contrib import admin
from blog.models import BlogMedia


class BlogMediaAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': ['title']}),
		(None,	{'fields': ['body']}),
		('Date information', {'fields': ['pub_date']}),
		(None,	{'fields': ['can_comment']}),
	]
	list_display = ('title', 'pub_date', 'was_published_recently', 'can_comment')
	search_fields = ['title']
	date_hierarchy = 'pub_date'

admin.site.register(BlogMedia, BlogMediaAdmin)
