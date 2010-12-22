# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib2
import re
from IncidentRATP.frontend.models import Incident, Line
from django.core.management.base import BaseCommand, CommandError

URL = "http://www.ratp.fr/informer/trafic/trafic.php?cat=%s"
RER = "2"
METRO = "1"
BUS_TRAM = "3"
TRANSILIEN = "4"
PATTERN = "<b>[A-Za-z -]*([0-9]*)[ :]*</b>([^\.]*)"

class Command(BaseCommand):
	args = ""
	help = "crawl ratp"
	
	def handle(self, *args, **options):
		compiled_pattern = re.compile(PATTERN)
		#metro :
		print "metro"
		consolidated_text = ""
		for line in urllib2.urlopen(URL % METRO):
			consolidated_text += line
		
		for result in compiled_pattern.findall(consolidated_text):
			(str_ligne, raison) = result
			incident = Incident()
			incident.line = Line.objects.get_or_create(name=str_ligne.strip())[0]
			incident.reason = raison.strip()
			incident.contributors = 'RATP'
		#rer :
		print "rer"
		consolidated_text = ""
		for line in urllib2.urlopen(URL % RER):
			consolidated_text += line

		for result in compiled_pattern.findall(consolidated_text):
			print result
		