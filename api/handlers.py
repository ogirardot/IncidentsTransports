#!/usr/bin/python
# -*- coding: utf-8 -*-
from piston.utils import throttle, rc
from piston.handler import BaseHandler
from frontend.models import Incident, Line, AddIncidentForm     
from django.shortcuts import render_to_response as render
from datetime import datetime, timedelta 
import re  
encoding = "ISO-8859-1"
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
	#fields = ('line', ('name',),), 'time', 'plus','minus', 'ended', 'id', 'reason')
		
   	@throttle(30, 60)
	def read(self, request, scope=None, incident_id=None):
		"""
        Returns a single post if `incident_id` is given,
        otherwise a subset.

        """
		base = Incident.objects
		
		if incident_id:
			incident = base.get(pk=incident_id)
			return {
                        'uid' : incident.id,
                        'line' : incident.line.name,
                        'line_id' : incident.line.id,
                        'last_modified_time' : incident.time,
                        'vote_plus' : incident.plus,
                        'vote_minus' : incident.minus,
                        'vote_ended' : incident.ended,
                        'status' : "Terminé" if incident.ended > 3 else "En cours...",
                        'reason' : incident.reason }
		else:
			if scope == "minute":
				filter_time = datetime.now() + timedelta(minutes=-1)
			elif scope == "hour":
				filter_time = datetime.now() + timedelta(hours=-1)
			elif scope == "day":    
				filter_time = datetime.now().date() 
			elif scope == "all":
				filter_time = None  
			elif scope == "current":
				filter_time = datetime.now() + timedelta(days=-1)  
			else:
				return []  
			if filter_time:
				return_objs = Incident.objects.filter(time__gte=filter_time).filter(validated=True).order_by('time').reverse()
			else:
				return_objs = Incident.objects.filter(validated=True).order_by('time').reverse()[:15] 
			# filter out terminated events
			if scope =="current":
				return_objs = [ incident for incident in return_objs if not incident.ended > 3]
			return [{
			'uid' : incident.id,
			'line' : incident.line.name,
			'line_id' : incident.line.id,
			'last_modified_time' : incident.time,
			'vote_plus' : incident.plus,
			'vote_minus' : incident.minus,
			'vote_ended' : incident.ended,
			'status' : "Terminé" if incident.ended > 3 else "En cours...",
			'reason' : incident.reason } for incident in return_objs] # Or base.filter(...)        

class LigneHandler(BaseHandler):
	allowed_methods = ('GET', )
	model = Line 
	fields = ('uid', 'name')
	@classmethod 
	def uid(klass, model): 
		return model.pk
                  
class IncidentCRUDHandler(BaseHandler):                 
	allowed_methods = ('POST',)
	model = Incident
	@throttle(5, 5*60)
	def create(self, request):   
		print "called with request %s " % (request.content_type)
		if request.content_type:
			try:                                    
				data = request.data                 
				if 'line_id' in data:
					line = Line.objects.get(pk=int(data['line_id']))
				else:
					line = Line.objects.get_or_create(name=data['line_name'].strip())[0]
				if not line:
					return rc.BAD_REQUEST                   
				# check for bad words :    
				comment = data['reason']
				source = data['source']
				incident = Incident(line=line, contributors=source, reason=comment)
				incident.save()   
				return incident.id  
			except:
				return rc.BAD_REQUEST
		else: 
			form = AddIncidentForm(request.POST) 
			if form.is_valid():
				form.save()
				return render('thanks.html', {'number': Incident.objects.count()}); 
			else:     
				resp = rc.BAD_REQUEST
				resp.write("Incorrect parameters, submitted form is invalid.")
				return resp
			
class IncidentVoteHandler(BaseHandler):
	allowed_methods = ('GET', 'POST')
	def read(self, request, incident_id, action): 
		if incident_id:   
			try:                       
				incident = Incident.objects.get(pk=incident_id)
				if action == "plus":
					return {"number": incident.plus}
				elif action == "minus":
					return {"number": incident.minus}
				elif action == "end":
					return {"number": incident.ended} 
				else: return rc.BAD_REQUEST
			except:
				return rc.BAD_REQUEST
		else: return rc.BAD_REQUEST    	

	def create(self, request, incident_id, action):  
		if incident_id:   
			try:                       
				incident = Incident.objects.get(pk=incident_id)
				if action == "plus":
					incident.plus += 1
					if incident.plus - incident.minus > 3 and not incident.validated:
						incident.validated = True
				elif action =="minus":
					incident.minus += 3
					if incident.minus - incident.plus > 1:
						incident.validated = False
				elif action == "end":
					incident.ended += 1
				comments = request.session.get('commented', None)
				if comments or incident.ended > 8:
					if incident.ended > 8 or str(incident.id) in comments.split(","): 
						return rc.ALL_OK
					else:
						incident.save()
						request.session['commented'] += "," + str(incident.id)
				else:
					incident.save()
					request.session['commented'] = str(incident.id)
				return rc.CREATED
			except Exception,e:
				print e
				return rc.BAD_REQUEST
		else: return rc.BAD_REQUEST
	            
			
			
			
			
			
			
			
			