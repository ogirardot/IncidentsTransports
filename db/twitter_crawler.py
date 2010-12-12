# -*- coding: utf-8 -*-
import urllib2
import re

URL = "http://search.twitter.com/search.json?lang=%s&q=%s&rpp=100"
LANG = "fr"
PATTERN = "#incidentratp[ ]*#ligne[ ]*([a-zA-Z0-9 ]*)#raison[ ]*([^#\"]*)"
TEST_STRING = u"#incidentratp #ligne metro 1 #raison aucune particulière"

def load():
	
	opened = urllib2.urlopen(URL % (LANG, "\%23incidentratp+\%23ligne+\%23raison"))
	aggregated_result = ""
	for line in opened:
		aggregated_result += line
	extract_re = re.compile(PATTERN)
	for line in extract_re.findall(aggregated_result):
		print line
	print "done"

def test_pattern():
	extract_re = re.compile(PATTERN)
	print extract_re.findall(TEST_STRING)
	
if __name__ == "__main__":
	test_pattern()
	load()