from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import *

incident_handler = Resource(IncidentHandler)
crud_incident_handler = Resource(IncidentCRUDHandler)    
ligne_handler = Resource(LigneHandler)
vote_handler = Resource(IncidentVoteHandler) 
duplicate_incident_handler = Resource(IncidentDuplicateHandler)

urlpatterns = patterns('',
   	url(r'^incidents.(?P<emitter_format>[a-z]+)/(?P<scope>[a-z]+)$', incident_handler),  
	url(r'^incident.(?P<emitter_format>[a-z]+)/(?P<incident_id>[\d]+)', incident_handler),
	url(r'^incident.(?P<emitter_format>[a-z]+)/vote/(?P<incident_id>[\d]+)/(?P<action>[a-z]+)', vote_handler),
	url(r'^incident/?$', crud_incident_handler),
	url(r'^incident/duplicate/?$', duplicate_incident_handler), 
	url(r'^ligne/?$', ligne_handler),
)
