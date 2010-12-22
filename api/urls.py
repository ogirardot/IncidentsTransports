from django.conf.urls.defaults import *
from piston.resource import Resource
from IncidentRATP.api.handlers import IncidentHandler

incident_handler = Resource(IncidentHandler)

urlpatterns = patterns('',
   url(r'^incidents.(?P<emitter_format>[a-z]+)/(?P<scope>[a-z]+)$', incident_handler),
)