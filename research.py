#!/usr/bin/env python

import sys
import json
import urllib
import urllib2

def main():
    argvs = sys.argv
    if validation_check(argvs):
      sys.exit(1)

    req = request_for_virustotal(argvs)
    receive_response(req)

def validation_check(argvs):
    argc = len(argvs)
    if (argc != 2):
        print 'Usage; python %s hash' % argvs[0]
        return True
    return False

def virus_total_url():
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    return url

def downloads_folder():
    folder_path = '/root/work/malware/downloads'
    return folder_path

def api_key():
    api_key_file_path = './api_key.txt'
    with open(api_key_file_path) as f:
      read = f.read()
      api_key = read.replace('\r', '')
      api_key = read.replace('\n', '')
      print 'api key:' + api_key
    return api_key

def generate_data(argvs):
    hash = argvs[1]
    parameters = {'resource': hash, 'apikey': api_key()}
    data = urllib.urlencode(parameters)
    return data

def request_for_virustotal(argvs):
    req = urllib2.Request(virus_total_url(), generate_data(argvs))
    return req

def display_response_json(j):
    data = json.loads(j)
    if data["response_code"] == 0:
        print "Result is FALSE. Please check your option."
    else:
        print "Scan is Success"

    for k, v in data.items():
        print str(k) + " :" + str(v)

def receive_response(req):
    response = urllib2.urlopen(req)
    response_read = response.read()
    display_response_json(response_read)

main()
