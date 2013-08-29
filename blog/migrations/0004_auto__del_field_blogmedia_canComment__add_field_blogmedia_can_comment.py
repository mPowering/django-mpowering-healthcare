# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BlogMedia.canComment'
        db.delete_column(u'blog_blogmedia', 'canComment')

        # Adding field 'BlogMedia.can_comment'
        db.add_column(u'blog_blogmedia', 'can_comment',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BlogMedia.canComment'
        db.add_column(u'blog_blogmedia', 'canComment',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'BlogMedia.can_comment'
        db.delete_column(u'blog_blogmedia', 'can_comment')


    models = {
        u'blog.blogmedia': {
            'Meta': {'object_name': 'BlogMedia'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'can_comment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']