# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ArticleImage'
        db.delete_table(u'blog_articleimage')

        # Adding field 'Article.image'
        db.add_column(u'blog_article', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='../blog/media/default.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ArticleImage'
        db.create_table(u'blog_articleimage', (
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blog', ['ArticleImage'])

        # Deleting field 'Article.image'
        db.delete_column(u'blog_article', 'image')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'can_comment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'../blog/media/default.jpg'", 'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']