import datetime, os, uuid
from django.db import models
from django.utils import timezone

from blog.widgets import AdvancedEditor


# Create your models here.
class Article(models.Model):
    
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (uuid.uuid4(), ext)
        print image_name       
        return "blog_imgs/%s" % image_name

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=generate_new_filename, default='blog_imgs/default.jpg')
    body = models.CharField(max_length=200)
    can_comment = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'  
