from django import forms
from blog.models import Article
from tinymce.widgets import TinyMCE
 
class ArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
 
    class Meta:
        model = Article