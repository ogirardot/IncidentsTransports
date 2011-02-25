from django.conf.urls.defaults import *
from piston.resource import Resource
from IncidentRATP.api.handlers import IncidentHandler, IncidentCRUDHandler

incident_handler = Resource(IncidentHandler)
crud_incident_handler = Resource(IncidentCRUDHandler)    

urlpatterns = patterns('',
   	url(r'^incidents.(?P<emitter_format>[a-z]+)/(?P<scope>[a-z]+)$', incident_handler),
	url(r'^incident/?$', crud_incident_handler),
)