# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column(u'blog_article', 'body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Article.image'
        db.alter_column(u'blog_article', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column(u'blog_article', 'body', self.gf('django.db.models.fields.CharField')(max_length=10000))

        # Changing field 'Article.image'
        db.alter_column(u'blog_article', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'can_comment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']