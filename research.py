#!/usr/bin/env python

import sys
import json
import urllib
import urllib2

def virus_total_url():
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    return url

def api_key():
    api_key = 'e7416f0e54656ee951c464471fdea80e33e89e859d798eb158fdd713f7646d72'
    return api_key

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage; python %s hash' % argvs[0]
  sys.exit(1)

hash = argvs[1]

url = virus_total_url()
parameters = {'resource': hash, 'apikey': api_key()}

data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json = response.read()
print json
