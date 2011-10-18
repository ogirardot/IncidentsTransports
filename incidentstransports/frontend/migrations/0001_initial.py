# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('frontend_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('frontend', ['City'])

        # Adding model 'Line'
        db.create_table('frontend_line', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('aliases', self.gf('django.db.models.fields.TextField')(default='')),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.City'])),
        ))
        db.send_create_signal('frontend', ['Line'])

        # Adding model 'Station'
        db.create_table('frontend_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('aliases', self.gf('django.db.models.fields.TextField')(default='')),
            ('line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Line'])),
        ))
        db.send_create_signal('frontend', ['Station'])

        # Adding model 'Incident'
        db.create_table('frontend_incident', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Line'], null=True)),
            ('station_start', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='station_start', null=True, to=orm['frontend.Station'])),
            ('station_end', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='station_end', null=True, to=orm['frontend.Station'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('ended', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.TextField')()),
            ('validated', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('duplicate_of', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Incident'], null=True, blank=True)),
        ))
        db.send_create_signal('frontend', ['Incident'])

        # Adding model 'IncidentVote'
        db.create_table('frontend_incidentvote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Incident'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('source', self.gf('django.db.models.fields.TextField')()),
            ('vote', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('frontend', ['IncidentVote'])


    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('frontend_city')

        # Deleting model 'Line'
        db.delete_table('frontend_line')

        # Deleting model 'Station'
        db.delete_table('frontend_station')

        # Deleting model 'Incident'
        db.delete_table('frontend_incident')

        # Deleting model 'IncidentVote'
        db.delete_table('frontend_incidentvote')


    models = {
        'frontend.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'frontend.incident': {
            'Meta': {'object_name': 'Incident'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duplicate_of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Incident']", 'null': 'True', 'blank': 'True'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Line']", 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'station_end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'station_end'", 'null': 'True', 'to': "orm['frontend.Station']"}),
            'station_start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'station_start'", 'null': 'True', 'to': "orm['frontend.Station']"}),
            'validated': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'frontend.incidentvote': {
            'Meta': {'object_name': 'IncidentVote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Incident']"}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'vote': ('django.db.models.fields.IntegerField', [], {})
        },
        'frontend.line': {
            'Meta': {'object_name': 'Line'},
            'aliases': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'frontend.station': {
            'Meta': {'object_name': 'Station'},
            'aliases': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Line']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['frontend']
