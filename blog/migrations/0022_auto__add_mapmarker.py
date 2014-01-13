# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MapMarker'
        db.create_table(u'blog_mapmarker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_of_region', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True)),
            ('link_more', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['MapMarker'])


    def backwards(self, orm):
        # Deleting model 'MapMarker'
        db.delete_table(u'blog_mapmarker')


    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'djangodbmodelsfieldscharfield'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.mapmarker': {
            'Meta': {'object_name': 'MapMarker'},
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_more': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_of_region': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'blog.presentation': {
            'Meta': {'object_name': 'Presentation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presentation_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.pressrelease': {
            'Meta': {'object_name': 'PressRelease'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'djangodbmodelsfieldscharfield'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.pressreleaselink': {
            'Meta': {'object_name': 'PressReleaseLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publication_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.report': {
            'Meta': {'object_name': 'Report'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'djangodbmodelsfieldscharfield'", 'max_length': '50'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "'me.jpg'", 'max_length': '200'}),
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