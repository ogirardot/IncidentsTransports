# -*- coding: utf-8 -*-
from django.db import models
from django import forms
    
class City(models.Model):
	name = models.CharField(max_length=255)
	
class Line(models.Model):
	name = models.CharField(max_length=255)
	aliases = models.TextField(default="")
	city = models.ForeignKey(City)
	def __unicode__(self):
		return "%s" % self.name     
		
class Station(models.Model):       
	name = models.CharField(max_length=255)
	aliases = models.TextField(default="")
	line = models.ForeignKey(Line)
	                                                        
class Incident(models.Model):  
	"""                   
	Incident representation of problems on the network 
	
	# create incident
	>>> i1 = Incident(line=Line.objects.get(pk=1), reason="Probleme dans le RER B", source="Android app", level=4)
	>>> i1.save()    
	   
	# try json shortcut :
	>>> i1.to_json()['status']
	'En cours...'
	>>> i1.to_json()['line_id']
	1
	>>> i1.to_json()['line']
	u'Metro 1'
	>>> i1.to_json()['vote_plus']
	0
	>>> i1.to_json()['vote_minus']
	0
	>>> i1.to_json()['vote_ended']
	0
	>>> i1.to_json()['uid']
	1
	>>> i1.to_json()['reason']
	'Probleme dans le RER B'
	
	# adding vote
	>>> IncidentVote(incident=i1, source="android1", vote=VOTE_PLUS).save() 
	>>> i1.plus_count()
	1
	
	# minus
	>>> IncidentVote(incident=i1, source="android2", vote=VOTE_MINUS).save()
	>>> i1.minus_count()
	3
	
	# ended
	>>> IncidentVote(incident=i1, source="android3", vote=VOTE_ENDED).save()
	>>> i1.ended_count()
	1
	"""
	line = models.ForeignKey(Line, blank=True, null=True, verbose_name="Ligne")
	station_start = models.ForeignKey(Station, null=True, blank=True, related_name="station_start")
	station_end = models.ForeignKey(Station, null=True, blank=True, related_name="station_end")
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	ended = models.DateTimeField(null=True, blank=True)
	reason = models.TextField("Raison", help_text="Raison évoquée quant à l'incident", blank=True, null=True)
	source = models.TextField()
	validated = models.BooleanField(default=True)  
	level = models.IntegerField(default=5)        
	
	def plus_count(self):
		return IncidentVote.objects.filter(incident=self).filter(vote=VOTE_PLUS).count()        
	def minus_count(self):
		return 3*IncidentVote.objects.filter(incident=self).filter(vote=VOTE_MINUS).count()
	def ended_count(self):           
		return IncidentVote.objects.filter(incident=self).filter(vote=VOTE_ENDED).count()    
	def to_json(self):
		return {'uid' : self.id,
    			'line' : self.line.name,
				'line_id' : self.line.id,
				'last_modified_time' : self.modified, 
				'creation_time': self.created,
				'end_time': self.ended,
				'vote_plus' : self.plus_count(),
				'vote_minus' : self.minus_count(),
				'vote_ended' : self.ended_count(),
				'status' : "Terminé" if self.ended_count() > 3 else "En cours...",
				'reason' : self.reason }
                                                                         
VOTE_PLUS = 1
VOTE_ENDED = 0
VOTE_MINUS = -1    

class IncidentVote(models.Model):
	incident = models.ForeignKey(Incident)
	created = models.DateTimeField(auto_now=True)
	source = models.TextField()
	vote = models.IntegerField()
			
class AddIncidentForm(forms.ModelForm):
	contributors = forms.EmailField(label="Email", help_text="Indiquez votre adresse email pour valider la sauvegarde") 
	class Meta:
		model = Incident
		fields = ('line', 'reason', 'contributors')