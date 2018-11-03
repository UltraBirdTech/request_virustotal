#!/usr/bin/env python

import sys
import json
import urllib
import urllib2

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage; python %s hash' % argvs[0]
  sys.exit(1)

hash = argvs[1]

url = "https://www.virustotal.com/vtapi/v2/file/report"
parameters = {"resource": hash, "apikey": "e7416f0e54656ee951c464471fdea80e33e89e859d798eb158fdd713f7646d72"}

data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json = response.read()
print json
