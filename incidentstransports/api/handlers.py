#!/usr/bin/python
# -*- coding: utf-8 -*-
from piston.utils import throttle, rc
from django.http import HttpResponse
from piston.handler import BaseHandler
from frontend.models import Incident, IncidentVote, Line, AddIncidentForm, VOTE_PLUS, VOTE_MINUS, VOTE_ENDED
from django.shortcuts import render_to_response as render
from datetime import datetime, timedelta
import logging
import sys
import re
encoding = "ISO-8859-1"

logger = logging.getLogger(__name__)

# this field is just to abstract the database impl
ORDER_FIELD_VALUES = {
'creation': 'created',
'modification': 'modified',
'end': 'ended'
}

class IncidentHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    @throttle(30, 60)
    def read(self, request, scope=None, incident_id=None, order_field='creation'):
        """
        Returns a single post if `incident_id` is given,
        otherwise a subset.
        
        """
        base = Incident.objects
                                           
        if incident_id:
            incident = base.get(pk=incident_id)
            return incident.to_json()
        else:
            if scope == "minute":
                filter_time = datetime.now() + timedelta(minutes=-1)
            elif scope == "hour":
                filter_time = datetime.now() + timedelta(hours=-1)
            elif scope == "day":
                now = datetime.now()
                filter_time = datetime(now.year, now.month, now.day, 0,0,0) + timedelta(hours=+3)   
            elif scope == "all":
                filter_time = None
            elif scope == "current":
                filter_time = datetime.now() + timedelta(days=-1)
            else:
                return []    
            # add order_field param from get request : 
            if 'sort_by' in request.GET:
                order_field = request.GET['sort_by']
                if order_field not in ORDER_FIELD_VALUES:
                    return rc.BAD_REQUEST 
                else:
                    pass
            
            if filter_time:
                return_objs = Incident.objects.filter(created__gte=filter_time).filter(validated=True).order_by(ORDER_FIELD_VALUES[order_field]).reverse()
            else:
                return_objs = Incident.objects.filter(validated=True).order_by(ORDER_FIELD_VALUES[order_field]).reverse()[:15]
            # filter out terminated events
            if scope =="current":
                return_objs = [ incident for incident in return_objs if not incident.ended_count() > 3]
            return [ incident.to_json() for incident in return_objs]

class LigneHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Line
    fields = ('uid', 'name')
    @classmethod
    def uid(klass, model):
        return model.pk

class IncidentCRUDHandler(BaseHandler):
    """
    This CRUD handler needs to be called with :
        * line_id or line_name
        * reason
        * source
        * level (int between 0 and 10, default is 5)
    """
    allowed_methods = ('POST',)
    model = Incident
    @throttle(5, 5*60)
    def create(self, request):
        """
        Throttled to create only 5 incidents by 5 minutes.
        """
        if request.content_type:
            try:
                data = request.data
                line = None
                if 'line_id' in data:
                    line = Line.objects.get(pk=int(data['line_id']))
                elif 'line_name' in data:
                    line = Line.objects.get_or_create(name=data['line_name'].strip())[0]
                if not line:
                    logger.error('Incident CRUD Handler got request with no line', exc_info=sys.exc_info(),
                      extra={
                          'request': request,
                          'url': request.build_absolute_uri(),
                          'data': {
                              'content_type': request.content_type,
                              'data': data
                          }
                      })
                    return rc.BAD_REQUEST
                comment = data['reason']
                source = data['source']
                incident = Incident(line=line, source=source, reason=comment)
                if 'level' in data:
                    incident.level = int(data['level'])
                incident.save()
                return HttpResponse(str(incident.id), status=201)
            except:
                logger.error('Incident CRUD Handler failed to process external request', exc_info=sys.exc_info(),
                      extra={
                          'request': request,
                          'url': request.build_absolute_uri(),
                          'data': {
                              'content_type': request.content_type,
                              'data': data
                          }
                      })
                return rc.BAD_REQUEST
        else:
            try:
                form = AddIncidentForm(request.POST)
                if form.is_valid():
                    form.save()            
                    return render('static/thanks.html', {'number': Incident.objects.count()});
                else:
                    resp = rc.BAD_REQUEST
                    resp.write("Incorrect parameters, submitted form is invalid.")
                    return resp
            except:     
                logger.error("Incident form submitted failed to be validated",
                             exc_info=sys.exc_info(), extra= {
                                 'request': request,
                                 'url': request.build_absolute_uri(),
                             })
                return rc.BAD_REQUEST

class IncidentVoteHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    def read(self, request, incident_id, action):
        if incident_id:
            try:
                incident = Incident.objects.get(pk=incident_id)
                if action == "plus":
                    return {"number": incident.plus_count()}
                elif action == "minus":
                    return {"number": incident.minus_count()}
                elif action == "end":
                    return {"number": incident.ended_count()}
                else: return rc.BAD_REQUEST
            except:
                return rc.BAD_REQUEST
        else: return rc.BAD_REQUEST
    
    def create(self, request, incident_id, action):   
        if incident_id:
            try:
                incident = Incident.objects.get(pk=incident_id)
                vote = IncidentVote(incident=incident)
                if 'source'in request.data:
                    vote.source = request.data['source']
                else:
                    vote.source = request.META['REMOTE_ADDR']
                
                if action == "plus":
                    vote.vote = VOTE_PLUS
                elif action =="minus":
                    vote.vote = VOTE_MINUS
                elif action == "end":
                    vote.vote = VOTE_ENDED
                comments = request.session.get('commented', None)
                if comments or incident.ended_count() > 8:
                    if incident.ended_count() > 8 or str(incident.id) in comments.split(","):
                        return rc.ALL_OK
                    else:
                        vote.save()
                        request.session['commented'] += "," + str(incident.id)
                else:
                    vote.save()
                    request.session['commented'] = str(incident.id)          
                                      
                # check afterwards if incident is invalid                 
                if 3*incident.minus_count() - incident.plus_count() > 1:
                    incident.validated = False
                incident.save()
        
                return rc.CREATED
            except Exception,e:
                print e
                return rc.BAD_REQUEST
        else: return rc.BAD_REQUEST
              
class IncidentDuplicateHandler(BaseHandler):
    allowed_methods = ('POST')  
    def create(self, request):
        if 'ref_id' in request.POST and 'duplicate_id' in request.POST:
            # sanity checks
            # existing incidents
            ref_count = Incident.objects.filter(pk=int(request.POST['ref_id'])).count()
            duplicate_count = Incident.objects.filter(pk=int(request.POST['duplicate_id'])).count()
            if not ref_count or not duplicate_count:
                logger.error('Incident Duplicate Handler - no existing incidents', exc_info=sys.exc_info(),
                      extra={
                          'request': request,
                          'url': request.build_absolute_uri(),
                          'ref_count' : ref_count,
                          'duplicate_count': duplicate_count,
                })
                return rc.NOT_FOUND                                                       
            ref = Incident.objects.get(pk=int(request.POST['ref_id']))
            duplicate = Incident.objects.get(pk=int(request.POST['duplicate_id']))
            # same line :    
            if ref.line != duplicate.line:
                return rc.BAD_REQUEST
            # same day :
            duplicate.duplicate_of = ref
            duplicate.save()
            return rc.CREATED
        else:  
            logger.error('Incident Duplicate Handler got bad request', exc_info=sys.exc_info(),
                  extra={
                      'request': request,
                      'url': request.build_absolute_uri()
                  })
            return rc.BAD_REQUEST
