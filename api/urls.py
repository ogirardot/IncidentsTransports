from django.conf.urls.defaults import *
from piston.resource import Resource
from IncidentRATP.api.handlers import IncidentHandler, IncidentCRUDHandler, LigneHandler

incident_handler = Resource(IncidentHandler)
crud_incident_handler = Resource(IncidentCRUDHandler)    
ligne_handler = Resource(LigneHandler)

urlpatterns = patterns('',
   	url(r'^incidents.(?P<emitter_format>[a-z]+)/(?P<scope>[a-z]+)$', incident_handler),
	url(r'^incident.(?P<emitter_format>[a-z]+)/(?P<incident_id>[\d]+)', incident_handler),
	url(r'^incident/?$', crud_incident_handler), 
	url(r'^ligne/?$', ligne_handler),
)
