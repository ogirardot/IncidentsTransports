#!/usr/bin/python
# -*- coding: utf-8 -*-
from piston.utils import throttle, rc
from piston.handler import BaseHandler
from frontend.models import Incident, Line, AddIncidentForm     
from django.shortcuts import render_to_response as render
from datetime import datetime, timedelta 
import re  

BAD_WORDS = " chier| connard| bite| chatte| cul " 
class IncidentWrapper(object):
	def __init__(uid, line_name, time, plus, minus, ended, reason):
		self.uid = uid
		self.time = time
		self.line = line_name
		self.plus = plus
		self.minus = minus
		self.ended = ended
		self.reason = reason 
		self.status = "Terminé" if self.ended > 3 else "En cours..."
		
class IncidentHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = (('line', ('name',),), 'time', 'plus','minus', 'ended', 'id', 'reason')
		
   	@throttle(5, 10*60)
	def read(self, request, scope, incident_id=None):
		"""
        Returns a single post if `incident_id` is given,
        otherwise a subset.

        """
		base = Incident.objects
		
		if incident_id:
			return base.get(pk=blogpost_id)
		else:
			if scope == "minute":
				filter_time = datetime.now() + timedelta(minutes=-1)
			elif scope == "hour":
				filter_time = datetime.now() + timedelta(hours=-1)
			elif scope == "day":
				filter_time = datetime.now() + timedelta(days=-1)
			return_objs = Incident.objects.filter(time__gte=filter_time).filter(validated=True)
			return return_objs # Or base.filter(...)        

class LigneHandler(BaseHandler):
	allowed_methods = ('GET', )
	model = Line 
	fields = ('uid', 'name')
	@classmethod 
	def uid(klass, model): 
		return model.pk
                  
class IncidentCRUDHandler(BaseHandler):                 
	allowed_methods = ('GET','POST',)
	model = Incident   
	fields = (('line', ('name',),), 'time', 'reason')  
	@throttle(3, 5*60)
	def create(self, request):
		if request.content_type:
			data = request.data 
			line = Line.objects.get(pk=int(data['line']))
			if not line:
				return rc.BAD_REQUEST                   
			# check for bad words :
			print "we'll deal with it"
			#comment = contributors
			#incident = Incident(line=line, contributors=)   
			return rc.CREATED
		else: 
			form = AddIncidentForm(request.POST) 
			if form.is_valid():
				form.save()
				return render('thanks.html', {'number': Incident.objects.count()}); 
			else:     
				resp = rc.BAD_REQUEST
				return resp
			