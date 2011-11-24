# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Incident.is_spam'
        db.add_column('frontend_incident', 'is_spam', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Incident.is_spam'
        db.delete_column('frontend_incident', 'is_spam')


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
            'is_spam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'aliases': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'aliases_rel_+'", 'null': 'True', 'to': "orm['frontend.Line']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_referential': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
