from django import forms
from blog.models import PressRelease, PressReleaseLink, Blog, Report, Presentation, Video, MapMarker
from tinymce.widgets import TinyMCE


class NewsArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = PressRelease


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    organization = forms.CharField(max_length=200, required=True) # potentially better to do label='Organization'
    email = forms.EmailField(required=True)


class NewsArticleLinkModelAdminForm(forms.ModelForm):
    class Meta:
        model = PressReleaseLink


class BlogModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Blog


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


class MapMarkerAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
   
    class Meta:
        model = MapMarker
