import datetime, os, uuid
from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Article(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (uuid.uuid1(), ext)
        return "%s%s" % (settings.BLOG_IMGS_ROOT, image_name)

    title = models.CharField(max_length=200)
    default_img_path = "%s%s" % (settings.BLOG_IMGS_ROOT, 'default.jpg')
    image = models.ImageField(upload_to=generate_new_filename, default=default_img_path)
    body = models.TextField()
    can_comment = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    class Meta:
        get_latest_by = "pub_date"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'


    @classmethod
    def get_latest_blogs(cls):
        return Article.objects.filter(can_comment=True).order_by("-pub_date").all()

    @classmethod
    def get_latest_news(cls):
        return Article.objects.filter(can_comment=False).order_by("-pub_date").all()
