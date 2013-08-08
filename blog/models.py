from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class BlogNews(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    # canComment = models.Boolean()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
