# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding model 'UserProfile'
        db.create_table(u'contacts_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('about', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=140)),
            ('reputation', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'contacts', ['UserProfile'])

        # Adding model 'Articles'
        db.create_table(u'contacts_articles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('time_stamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'contacts', ['Articles'])

        # Adding model 'Like'
        db.create_table(u'contacts_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Articles'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Like'])

        # Adding model 'Comment'
        db.create_table(u'contacts_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Articles'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'contacts', ['Comment'])

        # Adding model 'News'
        db.create_table(u'contacts_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'contacts', ['News'])

        # Adding model 'NewsContent'
        db.create_table(u'contacts_newscontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['NewsContent'])

        # Adding model 'ContactUs'
        db.create_table(u'contacts_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'contacts', ['ContactUs'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'UserProfile'
        db.delete_table(u'contacts_userprofile')

        # Deleting model 'Articles'
        db.delete_table(u'contacts_articles')

        # Deleting model 'Like'
        db.delete_table(u'contacts_like')

        # Deleting model 'Comment'
        db.delete_table(u'contacts_comment')

        # Deleting model 'News'
        db.delete_table(u'contacts_news')

        # Deleting model 'NewsContent'
        db.delete_table(u'contacts_newscontent')

        # Deleting model 'ContactUs'
        db.delete_table(u'contacts_contactus')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contacts.articles': {
            'Meta': {'object_name': 'Articles'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'contacts.comment': {
            'Meta': {'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Articles']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contacts.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contacts.like': {
            'Meta': {'object_name': 'Like'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Articles']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contacts.news': {
            'Meta': {'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'contacts.newscontent': {
            'Meta': {'object_name': 'NewsContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reputation': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '140'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']