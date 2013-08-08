from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class BlogMedia(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    can_comment = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'
