#!/usr/bin/env python

import sys
import json
import urllib
import urllib2
import hashlib
import glob
from datetime import datetime
import os

def main():
    print 'START SCRIPT'

    file_array = glob.glob(check_folder_path() + '*')
    i = 0 
    result_array = []

    for file in file_array:
       i += 1
       with open(file, 'rb') as f:
           hash = hashlib.sha256(f.read()).hexdigest()
           req = request_for_virustotal(hash)
           res = recieve_response(req)
           res_json = json.loads(res)
           permalink = res_json["permalink"]
           file_detection_rate =  str(res_json["positives"]) + '/' + str(res_json["total"])
           file_name = f.name.split("/")[-1]

           time_float = os.path.getmtime(check_folder_path() + file_name)
           file_timedate = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")
           result_array.append("|" + file_name + "|" + file_timedate + "|" + file_detection_rate + "|" + permalink + "|")
           if 3 < i:
             break

    generate_output_file(result_array) 
    print 'END SCRIPT'
    exit()

def check_folder_path():
    return '/root/work/malware/downloads/malware/'

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

def generate_data(data):
    hash = data 
    parameters = {'resource': hash, 'apikey': api_key()}
    data = urllib.urlencode(parameters)
    return data

def request_for_virustotal(data):
    req = urllib2.Request(virus_total_url(), generate_data(data))
    return req

def recieve_response(req):
    response = urllib2.urlopen(req)
    response_read = response.read()
    return response_read

def generate_file_name():
    return 'virus_total_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'

def header():
    return '|file name|date| kensyuturitu| URL |'

def constitution():
    return '|:--|:--|:--:|:--|'

def generate_output_file(array):
    f = open(generate_file_name(), 'w')
    f.writelines(header() + "\n")
    f.writelines(constitution() + "\n")
    for line in array:
        f.writelines(line + "\n")
    
    f.close()
main()
