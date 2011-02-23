# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import urllib2
import re
import json
from IncidentRATP.frontend.models import Incident, Line
from django.core.management.base import BaseCommand, CommandError

URL = "http://search.twitter.com/search.json?lang=%s&q=%s&rpp=100"
LANG = "fr"
PATTERN = "#incidentratp[ ]*#ligne[ ]*([a-zA-Z0-9 ]*)#raison[ ]*([^#\"\.]*)"
TEST_STRING = u"#incidentratp #ligne metro 1 #raison aucune particulière"
class Command(BaseCommand):
	args = ""
	help = "crawl twitter"
	
	def handle(self, *args, **options):
		opened = urllib2.urlopen(URL % (LANG, "\%23incidentratp+\%23ligne+\%23raison"))
		aggregated_result = ""
		for line in opened:
			aggregated_result += line
	#	print "result : %s " % (aggregated_result)
		extract_re = re.compile(PATTERN)
		loaded_document = json.loads(aggregated_result)
		for line in loaded_document['results']:
			try:
				print line['id_str'], 
				(str_ligne, raison) = extract_re.findall(line['text'])[0]
				incident = Incident()
				ligne = Line.objects.get_or_create(name=str_ligne.strip().upper())[0]
				incident.line = ligne
				incident.reason = raison.strip()
				incident.contributors = '(%s, %s)' % (line['id_str'], line['from_user'])
				# test if incident exist
				incidents = Incident.objects.filter(line=ligne).filter(contributors__icontains = incident.contributors)
				if len(incidents) != 0:
					continue
					print "existing"
					incident = incidents[0]
					incident.plus += 1
					incident.contributors += ',(%s, %s)' % (line['id_str'], line['from_user'])
				incident.save()
			except Exception as e:
				print str(e)
		print "done"