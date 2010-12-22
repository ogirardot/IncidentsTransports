from piston.handler import BaseHandler
from frontend.models import Incident
from datetime import datetime, timedelta

class IncidentHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Incident   
   fields = (('line', ('name',),), 'time', 'reason')

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