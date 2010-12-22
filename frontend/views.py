from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import render_to_response as render
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from models import Station, Line, Incident, AddIncidentForm

def index(request):
	return render('index.html')
	
def dev(request):
	return render('dev.html')

def incidents(request):
	return render('incidents.html')

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

def contact(request):
	return render('contact.html')

def incident_interact(request, action):
	return render('contact.html')

def add_incident(request):
	if request.method == "POST":
		form = AddIncidentForm(request.POST)
		form.save()
		return render('thanks.html', {'number' : Incident.objects.count()})
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
		incident.minus += 1
		if incident.minus - incident.plus > 3:
			incident.validated = False
		out = incident.minus
	elif action == "end":
		incident.ended += 1
		if incident.ended > 3:
			incident.validated = False
		out = incident.ended
	incident.save()
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