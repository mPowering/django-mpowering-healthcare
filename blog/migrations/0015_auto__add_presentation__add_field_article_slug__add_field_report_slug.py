# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.slug'
        db.add_column(u'blog_article', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug-title-goes-here', max_length=50),
                      keep_default=False)

        # Adding field 'Report.slug'
        db.add_column(u'blog_report', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug-title-goes-here', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.slug'
        db.delete_column(u'blog_article', 'slug')

        # Deleting field 'Report.slug'
        db.delete_column(u'blog_report', 'slug')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'can_comment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'slug-title-goes-here'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.presentation': {
            'Meta': {'object_name': 'Presentation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presentation_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.report': {
            'Meta': {'object_name': 'Report'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'slug-title-goes-here'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.video': {
            'Meta': {'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']