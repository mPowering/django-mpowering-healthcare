from django import forms
from blog.models import NewsArticle, NewsArticleLink, Blog, Report, Presentation, Video
from tinymce.widgets import TinyMCE


class NewsArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = NewsArticle


class NewsArticleLinkModelAdminForm(forms.ModelForm):
    blurb = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = NewsArticleLink


class BlogModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Blog


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    organisation = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)


class ReportModelAdminForm(forms.ModelForm):
    class Meta:
        model = Report


class PresentationModelAdminForm(forms.ModelForm):
    class Meta:
        model = Presentation


class VideoModelAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Video
