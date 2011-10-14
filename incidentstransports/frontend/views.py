import random, re
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from models import Station, Line, Incident, IncidentVote, VOTE_PLUS, VOTE_MINUS, VOTE_ENDED, AddIncidentForm
from frontend.utils import render
	
def handler_404(request):
	images = ["1293872626292.jpg", "1293878551093.jpg" ]
	legendes = ["Mais pourquoi sont-ils aussi mechant ?!", "rien a dire d'autre..."]
	pick_a_number = random.randint(0, len(images))-1
	return render(request, '404.html' , { 'image' : images[pick_a_number], 'legende' : legendes[pick_a_number]})
	                       
def load_test(request):
	return HttpResponse("42")
                                           
def stats(request, template_name="stats.html"):
	def extract_date(entity):
		return entity.created.date()
		  
	entities = Incident.objects.order_by('created')
	                              
	from itertools import groupby
	data = [len(list(g)) for t, g in groupby(entities, key=extract_date)]                      
	labels = []
	return render(request, template_name, {'data': data,'labels': labels})    
                  	                                
def add_incident(request, template_name="incidents/add_incident.html"):
	if request.method == "POST":
		form = AddIncidentForm(request.POST)
		if form.is_valid() and not re.search(" chier| connard| bite| chatte| cul", form['reason'].data) :
			form.save()
			return render(request, 'static/thanks.html', {'number' : Incident.objects.count()})
		else:
			return render(request, template_name, {'form' : form})
	else:
		form = AddIncidentForm()
		return render(request, template_name, {'form' : form})

def incident_interact(request, id, action):
	incident = Incident.objects.get(id=id)  
	vote = IncidentVote(incident=incident)
	vote.source = request.META['REMOTE_ADDR']
	out= ""
	if action == "plus":
		vote.vote = VOTE_PLUS
		if incident.plus_count() + 1 - incident.minus_count() > 3 and not incident.validated:
			incident.validated = True
		out = incident.plus_count() + 1
	elif action =="minus":
		vote.vote = VOTE_MINUS
		if incident.minus_count() - 3 - incident.plus_count() > 1:
			incident.validated = False   
		out = incident.minus_count() + 3
	elif action == "end":
		vote.vote = VOTE_ENDED
		out = incident.ended_count() + 1
	comments = request.session.get('commented', None)
	if comments or incident.ended_count() > 8:
		if incident.ended_count() > 8 or str(incident.id) in comments.split(","): 
			if action =="minus":
				return HttpResponse(str(out-3))   
			else:
				return HttpResponse(str(out-1))
		else:   
			incident.save()
			vote.save()
			request.session['commented'] += "," + str(incident.id)
	else:
		incident.save()  
		vote.save()
		request.session['commented'] = str(incident.id)
	return HttpResponse(str(out))
	
def get_incidents(request, scope, template_name="incidents/get_incidents.html"):
	return_objs = []
	filter_time = None
	if scope == "minute":
		filter_time = datetime.now() + timedelta(minutes=-1)
	elif scope == "hour":
		filter_time = datetime.now() + timedelta(hours=-1)
	elif scope == "day":
		filter_time = datetime.now() + timedelta(days=-1)
	else:
		return render('index.html')
	return_objs = Incident.objects.filter(modified__gte=filter_time).filter(validated=True).order_by('created').reverse()
	return render(request, template_name, {'incidents' : return_objs, 'scope':scope})

def get_incident(request, incident_id, 
		year=None, 
		month=None, 
		day=None, 
		line_slug=None, 
		line_id=None, 
		incident_slug=None, 
		template_name="incidents/detail_incident.html"):
	incident = get_object_or_404(Incident, pk=incident_id)                      
	return render(request, template_name, {'incident' :  incident}) 

def disqus_mobile(request, id, template_name="disqus.html"):
	incident = get_object_or_404(Incident, pk=id)                      
	return render(request, template_name, {'incident' :  incident}) 	   
	
def archives(request, template_name="incidents/archives.html"):                                       
	return render(request, template_name, {'incidents': Incident.objects.all() })
