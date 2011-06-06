from django.test.client import Client     
from frontend.models import Incident, Line, City
import unittest
import re

class IncidentTransportsAPITestCase(unittest.TestCase):
	def test_get_incidents(self):
		c = Client()
		respo = c.get("/api/incidents.json/day")
		self.assertEqual(respo.status_code, 200)
		                       
	def test_get_incident(self):            
		# init incident :
		i1 = Incident(line=Line.objects.get(pk=1), reason="Probleme dans le RER B", source="Android app", level=4)
		i1.save()    
		
		c = Client()
		respo = c.get("/api/incident.json/%s" % (i1.pk))
		self.assertEqual(respo.status_code, 200)
		
	def test_get_lignes(self):
		# init ligne :                                   
		c1 = City(name="Jaichi")                                   
		c1.save()
		l1 = Line(name="Line Ichiban", aliases="L1, LI1", city=c1)
		l1.save()
		
		c = Client()
		respo = c.get("/api/ligne")
		self.assertEqual(respo.status_code, 200)  
		self.assertTrue('{ "name": "Line Ichiban", "uid": 20 }' in re.sub(r"[\r\n ]+", r" ", respo.content.strip()))
	
	#ignored because test limit reached
	#def test_get_incorrect_incident(self):
	#	c = Client()
	#	respo = c.get("/api/incident.json/1337")
	#	self.assertEqual(respo.status_code, 500)
		
	def test_post_incident(self):  
		c = Client()                                                                                                  
		# this is bad request, no content_type
		respo = c.post("/api/incident", {'line_id' : 1, 'reason': "my heart know my reasons", 'source':"test_client"}, content_type="")
		self.assertEqual(respo.status_code, 400)
		                        
		c = Client()
		# this is good request :
		respo = c.post(path="/api/incident", data={'line_id' : 1, 'reason': "my heart know my reasons", 'source':"test_client"})
		self.assertEqual(respo.status_code, 201)
		
		incident_id = int(respo.content)
		respo = c.get("/api/incident.json/%s" % incident_id)
		self.assertEqual(respo.status_code, 200)
		
class IncidentTransportsThrottleTestCase(unittest.TestCase):
	def test_throttle(self):
		c = Client()              
		for i in range(24):
			respo = c.get("/api/incidents.json/all")
			self.assertEqual(respo.status_code, 200)
                         
		respo = c.get("/api/incidents.json/all")
		self.assertEqual(respo.status_code, 503)
		
		   	