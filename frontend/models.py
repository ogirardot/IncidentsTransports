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
	
	def plus(self):
		return IncidentVote.objects.filter(incident=self).filter(vote=VOTE_PLUS).count()        
	def minus(self):
		return IncidentVote.objects.filter(incident=self).filter(vote=VOTE_MINUS).count()
	def ended(self):           
		return IncidentVote.objects.filter(incident=self).filter(vote=VOTE_ENDED).count()
                                                                         
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