#!/usr/bin/env python

import sys
import json
import urllib
import urllib2

def virus_total_url():
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    return url

def api_key():
    api_key_file_path = './api_key.txt'
    api_key = ''
    with open(api_key_file_path) as f:
      api_key = f.read()
      api_key_replace = api_key.replace('\r', '')
      api_key_replace = api_key.replace('\n', '')
    return api_key_replace

def request_for_virustotal(data):
    req = urllib2.Request(virus_total_url(), data)
    return req

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage; python %s hash' % argvs[0]
  sys.exit(1)

hash = argvs[1]

parameters = {'resource': hash, 'apikey': api_key()}
print 'api key:' + api_key()

data = urllib.urlencode(parameters)
req = request_for_virustotal(data)
response = urllib2.urlopen(req)
json = response.read()
print json
