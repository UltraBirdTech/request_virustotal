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
#    print file_array

    i = 0 
    result_array = []
    print '1'

    for file in file_array:
       i += 1
     #  print file
      # print i
       print 'kiteru'
       with open(file, 'rb') as f:
           hash = hashlib.sha256(f.read()).hexdigest()
       #    print hash
      #     hash_array.append(hash)
           req = request_for_virustotal(hash)
           res = recieve_response(req)
         #  print res
           res_json = json.loads(res)
           permalink = res_json["permalink"]
           print res_json["permalink"]
           file_detection_rate =  str(res_json["positives"]) + '/' + str(res_json["total"])
           print str(res_json["total"]) + '/' + str(res_json["positives"])
           file_name = f.name.split("/")[-1]
           print file_name

           time_float = os.path.getmtime(check_folder_path() + file_name)
           file_timedate = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")
           print file_timedate
           print result_array
           result_array.append("|" + file_name + "|" + file_timedate + "|" + file_detection_rate + "|" + permalink )
           print result_array
           break

    generate_output_file(result_array) 
    print 'END SCRIPT'
    exit()

    req = request_for_virustotal(argvs[1])
    recieve_response(req)

def validation_check(argvs):
    argc = len(argvs)
    if (argc != 2):
        print 'Usage; python %s hash' % argvs[0]
        return True
    return False

def check_folder_path():
    return '/root/work/malware/downloads/malware/'

def read_files():
    path = check_folder_path()

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

def display_response_json(j):
    data = json.loads(j)
    if data["response_code"] == 0:
        print "Result is FALSE. Please check your option."
    else:
        print "Scan is Success"

    for k, v in data.items():
        print str(k) + " :" + str(v)

def recieve_response(req):
    response = urllib2.urlopen(req)
    response_read = response.read()
#    display_response_json(response_read)
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
