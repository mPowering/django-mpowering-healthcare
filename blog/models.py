import datetime, os
from django.db import models
from django.utils import timezone
import time


# Create your models here.
class Article(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (int(time.time() * 100000), ext)
        return "%s%s%s" % ("blog_imgs", os.sep, image_name)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=generate_new_filename,
                              max_length=200)
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


class Report(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (int(time.time() * 100000), ext)
        return "%s%s%s" % ("blog_imgs", os.sep, image_name)

    title = models.CharField(max_length=200)
    item = models.FileField(upload_to=generate_new_filename,
                              max_length=200)
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
    def get_latest_reports(cls):
        return Report.objects.order_by("-pub_date").all()


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.video_id

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'


    @classmethod
    def get_latest_videos(cls):
        return Video.objects.order_by("-pub_date").all()
