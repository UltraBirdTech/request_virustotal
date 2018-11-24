#!/usr/bin/env python

import sys
import json
import urllib
import urllib2
import hashlib
import glob
from datetime import datetime
from time import sleep
import os

MALWARE_DIR = '/root/work/malware/home/honey/downloads/malware/'
VIRUS_TOTAL_REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'

def main():
    print 'START SCRIPT'
    file_array = sorted(glob.glob( MALWARE_DIR + '*'), key=os.path.getmtime)
    print '[log]File num is: ' + str(len(file_array))
    result_array = []
    for i, file in enumerate(file_array):
       with open(file, 'rb') as f:
           malware = MalwareFile(f)
           print '[LOG] Check: ' + malware.file_name
       virus_total = VirusTotal()
       virus_total.request(malware)
       result_array.append(malware.generate_row())
       if (i + 1) % 4 == 0:
           print '[LOG] Sleep 65 seconds.'
           sleep(65)
    output_file = OutputFile()
    output_file.generate(result_array)
    print 'END SCRIPT'

class MalwareFile:
    def __init__(self, f):
        self.file_name = f.name.split("/")[-1]
        self.sha256 = hashlib.sha256(f.read()).hexdigest()
        # check file datetime.
        time_float = os.path.getmtime(MALWARE_DIR + self.file_name)
        self.datetime = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")
        self.detection_rate = '-'
        self.permalink = '-'

    def set_permalink(self, data):
        self.permalink = data["permalink"]

    def set_detection_rate(self, data):
        self.detection_rate =  str(data["positives"]) + '/' + str(data["total"])

    def generate_row(self):
        return "|" + self.file_name + "|" + self.datetime + "|" + self.detection_rate + "|" + self.permalink + "|"

class OutputFile:
    def generate(self, array):
        with open(self.generate_file_name(), 'w') as f:
            f.writelines(self.header() + "\n")
            f.writelines(self.constitution() + "\n")
            for line in array:
                f.writelines(line + "\n")

    def generate_file_name(self):
        return 'virus_total_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'

    def header(self):
        return '|file name|date| kensyuturitu| URL |'

    def constitution(self):
        return '|:--|:--|:--:|:--|'

class VirusTotal():
    def request(self, malware):
        parameters = {'resource': malware.sha256, 'apikey': api_key()}
        data = urllib.urlencode(parameters)
        request = urllib2.Request(VIRUS_TOTAL_REPORT_URL, data)
        response = urllib2.urlopen(request)
        res_json = json.loads(response.read())

        if res_json['response_code'] == 0:
            print '===================[LOG] RESPONSE CODE IS 0.======================'
            print res_json
        else:
            malware.set_permalink(res_json)
            malware.set_detection_rate(res_json)

    # read api_key from ./api_key.txt
    def api_key():
        api_key_file_path = './api_key.txt'
        with open(api_key_file_path) as f:
          read = f.read()
          api_key = read.replace('\n', '')
        return api_key

main()
