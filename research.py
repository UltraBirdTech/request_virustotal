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

def generate_data():
    hash = argvs[1]
    parameters = {'resource': hash, 'apikey': api_key()}
    data = urllib.urlencode(parameters)
    return data

def request_for_virustotal():
    req = urllib2.Request(virus_total_url(), generate_data())
    return req

def display_response_json(j):
    print j
    data = json.loads(j)
    if data["response_code"] == 0:
        print "Result is FALSE. Please check your option."
    else:
        print "Scan is Success"

    for k, v in data.items():
        print str(k) + " :" + str(v) 

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage; python %s hash' % argvs[0]
  sys.exit(1)

print 'api key:' + api_key()

req = request_for_virustotal()
response = urllib2.urlopen(req)
json = response.read()
# json = {"response_code": 0, "resource": "aa", "verbose_msg": "Invalid resource, check what you are submitting"} 
display_response_json(json)
#print json
