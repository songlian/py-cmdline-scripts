#!/usr/bin/python

import httplib
import urllib
import simplejson
import sys

DEGREE_SYMBOL=u'\u00B0'

if len(sys.argv) != 2:
	print 'Usage: yahoo-weather.py [zipcode]'
	sys.exit(0)

conn = httplib.HTTPConnection("query.yahooapis.com")
conn.request("GET", "/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20location%3D%22" + sys.argv[1] + "%22&format=json")
response = conn.getresponse()
query = simplejson.loads(response.read());
weather = query['query']['results']['channel']['item']['condition']
title = query['query']['results']['channel']['item']['title']
print title + " " + weather['temp'] + DEGREE_SYMBOL + "F" + " " + weather['text']
conn.close()

