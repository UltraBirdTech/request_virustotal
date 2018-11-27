#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib
import urllib2
import hashlib
import glob
from datetime import datetime
from time import sleep
import os
import subprocess

MALWARE_DIR = '/root/work/malware/home/honey/downloads/malware/'

def main():
    print 'START SCRIPT'
    file_array = sorted(glob.glob( MALWARE_DIR + '*'), key=os.path.getmtime)
    print '[LOG] File num is: ' + str(len(file_array))
    malwares = []
    virus_total = VirusTotal()
    for i, file in enumerate(file_array):
       with open(file, 'rb') as f:
           malware = MalwareFile(f)
           print '[LOG] Check: ' + malware.file_name
       virus_total.request(malware)
       malwares.append(malware)
       if (i + 1) % 4 == 0:
           print '[LOG] Sleep 65 seconds.'
           sleep(65)
    output_file = OutputFile()
    output_file.generate(malwares)
    print 'END SCRIPT'

#################################
# マルウェアクラス
# __init__() f: file information
class MalwareFile:
    def __init__(self, f):
        self.file_name = f.name.split("/")[-1]
        self.sha256 = hashlib.sha256(f.read()).hexdigest()
        self.set_datetime()
        self.detection_rate = '-'
        self.permalink = '-'
        self.set_file_type()

    def set_datetime(self):
        time_float = os.path.getmtime(MALWARE_DIR + self.file_name)
        self.datetime = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")

    def set_permalink(self, data):
        self.permalink = data['permalink']

    def set_detection_rate(self, data):
        self.detection_rate =  str(data['positives']) + '/' + str(data['total'])

    def set_file_type(self):
        proc = subprocess.Popen("file " + MALWARE_DIR + self.file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        file_type = proc.stdout.readline()
        proc.poll()
        file_type_split = file_type.split(":")[-1]
        self.file_type = file_type_split.split(",")[0]

####################################
# Output File Class
# generate output file for paste a article.
class OutputFile:
    def generate(self, malwares):
        with open(self.generate_file_name(), 'w') as f:
            f.writelines('Total: ' + str(len(malwares)) + "\n")
            f.writelines(self.header() + "\n")
            f.writelines(self.constitution() + "\n")
            for malware in malwares:
                f.writelines(self.generate_row(malware) + "\n")

    def generate_file_name(self):
        # like 'virus_total_20180000000000.txt'
        return 'virus_total_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'

    def header(self):
        return '| ファイル名 | file type | 取得日時 | 検出率 | URL |'

    def constitution(self):
        return '|:--|:--|:--|:--:|:--|'

    def generate_row(self, malware):
        return '|' + malware.file_name + '|'+ malware.file_type  + '|' + malware.datetime + '|' + malware.detection_rate + '|' + malware.permalink + '|'

class VirusTotal():
    VIRUS_TOTAL_REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'
    def __init__(self):
        self.api_key = self.api_key()
        print '[LOG] api key: ' + self.api_key

    def request(self, malware):
        parameters = {'resource': malware.sha256, 'apikey': self.api_key}
        data = urllib.urlencode(parameters)
        request = urllib2.Request(self.VIRUS_TOTAL_REPORT_URL, data)
        response = urllib2.urlopen(request)
        res_json = json.loads(response.read())

        if res_json['response_code'] == 0:
            print '[LOG] RESPONSE CODE IS 0.'
            print res_json
        else:
            malware.set_permalink(res_json)
            malware.set_detection_rate(res_json)

    # read api_key from ./api_key.txt
    def api_key(self):
        api_key_file_path = './api_key.txt'
        with open(api_key_file_path) as f:
          read = f.read()
          api_key = read.replace('\n', '')
        return api_key

main()

