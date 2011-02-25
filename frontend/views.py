import random
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import get_object_or_404, render_to_response as render
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from models import Station, Line, Incident, AddIncidentForm

def index(request):
	return render('index.html')
	
def handler_404(request):
	images = ["1293872626292.jpg", "1293878551093.jpg" ]
	legendes = ["Mais pourquoi sont-ils aussi mechant ?!", "rien a dire d'autre..."]
	pick_a_number = random.randint(0, len(images))-1
	return render('404.html' , { 'image' : images[pick_a_number], 'legende' : legendes[pick_a_number]})
	
def dev(request):
	return render('dev.html')

def incidents(request):
	return render('incidents.html')
                              
def stats(request):
	def extract_date(entity):
		return entity.time.date()
		  
	entities = Incident.objects.order_by('time')
	                              
	from itertools import groupby
	data = [len(list(g)) for t, g in groupby(entities, key=extract_date)]                      
	labels = []
	return render('stats.html', {'data': data,'labels': labels})    

def contribute(request):
	return render('contribute.html')

def services(request):
	return render('contribute.html')

def about(request):
	return render('team.html')

def contribute_donate(request):
	return render('donate.html')

def contribute_twitter(request):
	return render('twitter.html')

def add_incident(request):
	if request.method == "POST":
		form = AddIncidentForm(request.POST)
		if form.is_valid() and ("bite" not in form['reason'].data) :
			form.save()
			return render('thanks.html', {'number' : Incident.objects.count()})
		else:
			return render('add_incident.html', {'form' : form})
	else:
		form = AddIncidentForm()
		return render('add_incident.html', {'form' : form})

def incident_interact(request, id, action):
	incident = Incident.objects.get(id=id)    
	out = ""
	if action == "plus":
		incident.plus += 1
		if incident.plus - incident.minus > 3 and not incident.validated:
			incident.validated = True
		out = incident.plus
	elif action =="minus":
		incident.minus += 3
		if incident.minus - incident.plus > 1:
			incident.validated = False
		out = incident.minus
	elif action == "end":
		incident.ended += 1
		out = incident.ended
	comments = request.session.get('commented', None)
	if comments or incident.ended > 8:
		if incident.ended > 8 or str(incident.id) in comments.split(","): 
			if action =="minus":
				return HttpResponse(str(out-3))   
			else:
				return HttpResponse(str(out-1))
		else:
			incident.save()
			request.session['commented'] += "," + str(incident.id)
	else:
		incident.save()
		request.session['commented'] = str(incident.id)
	return HttpResponse(str(out))
	
def get_incidents(request, scope):
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
	return_objs = Incident.objects.filter(time__gte=filter_time).filter(validated=True).order_by('time').reverse()
	return render('get_incidents.html', {'incidents' : return_objs, 'scope':scope})

def get_incident(request, id):
	incident = get_object_or_404(Incident, pk=id)                      
	return render('detail_incident.html', {'incident' :  incident}) 
