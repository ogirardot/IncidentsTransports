# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class Line(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return "%s" % self.name
		
class Station(models.Model):
	name = models.CharField(max_length=255)
	line = models.ForeignKey(Line)
	
class Incident(models.Model):
	line = models.ForeignKey(Line, blank=True, null=True, verbose_name="Ligne")
	station = models.ForeignKey(Station, blank=True, null=True)
	time = models.DateTimeField(auto_now=True)
	plus = models.IntegerField(default=0)
	minus = models.IntegerField(default=0)
	ended = models.IntegerField(default=0)
	reason = models.TextField("Raison", help_text="Raison évoquée quant à l'incident", blank=True, null=True)
	contributors = models.TextField()
	validated = models.BooleanField(default=True)
	
	def __unicode__(self):
		return "Incident<%s, %s>" % (str(self.line), self.time)
		
class AddIncidentForm(forms.ModelForm):
	contributors = forms.EmailField(label="Email", help_text="Indiquez votre adresse email pour valider la sauvegarde") 
	class Meta:
		model = Incident
		fields = ('line', 'reason', 'contributors')