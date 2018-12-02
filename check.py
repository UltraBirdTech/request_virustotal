#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib
import urllib2
import hashlib
import glob
from datetime import datetime
from datetime import timedelta
from time import sleep
import os
import subprocess

MALWARE_DIR = './downloads/malware/'

def main():
    print 'START SCRIPT'
    file_array = sorted(glob.glob( MALWARE_DIR + '*'), key=os.path.getmtime)
    malwares = []
    virus_total = VirusTotal()
    for file in file_array:
       with open(file, 'rb') as f:
           malware = MalwareFile(f)

       if malware.check_date():
           if virus_total.check_request_time():
               print '[LOG] Sleep 65 seconds.'
               sleep(65)

           print '[LOG] Check: ' + malware.file_name
           virus_total.request(malware)
           malwares.append(malware)
       else:
           print '[LOG] Skip: ' + malware.file_name

    output_file = OutputFile()
    output_file.generate(malwares)
    print 'END SCRIPT'

#################################
# マルウェアクラス
# __init__() f: file information
class MalwareFile:
    def __init__(self, f):
        self.set_file_name(f)
        self.set_sha_256(f)
        self.set_datetime()
        self.set_file_type()
        self.kind = '-'

    def set_file_name(self, f):
        self.file_name = f.name.split("/")[-1]

    def set_sha_256(self, f):
        self.sha256 = hashlib.sha256(f.read()).hexdigest()

    def set_datetime(self):
        time_float = os.path.getmtime( MALWARE_DIR + self.file_name)
        self.datetime = datetime.fromtimestamp(time_float).strftime("%Y/%m/%d %H:%M:%S")

    def set_file_type(self):
        proc = subprocess.Popen("file " + MALWARE_DIR + self.file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        file_type = proc.stdout.readline()
        proc.poll()
        file_type_split = file_type.split(":")[-1]
        self.file_type = file_type_split.split(",")[0]

    def set_permalink(self, data):
        self.permalink = data['permalink'] if ('permalink' in data) else '-'

    def set_detection_rate(self, data):
        self.detection_rate = str(data['positives']) + '/' + str(data['total']) if ('positives' in data) else '-'

    def set_file_kind(self, data):
        #something code
        #Output; Torjian, DDos Script
        #Check response code.
        print self
        print data
        exit()

    def check_date(self):
        week_ago_date = datetime.now().date() + timedelta(weeks=-1)
        file_date = datetime.strptime(self.datetime,'%Y/%m/%d %H:%M:%S').date()
        return week_ago_date <= file_date

####################################
# Output File Class
# generate output file for paste a article.
class OutputFile:
    def generate(self, malwares):
        with open(self.generate_file_name(), 'w') as f:
            f.writelines('Total: ' + str(len(malwares)) + "\n")
            f.writelines("\n")
            f.writelines(self.header() + "\n")
            f.writelines(self.constitution() + "\n")
            for malware in malwares:
                f.writelines(self.generate_row(malware) + "\n")

    def generate_file_name(self):
        # like 'virus_total_20180000000000.txt'
        return 'virus_total_' + str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'

    def header(self):
        return '| ファイル名 | タイプ | 取得日時 | 検出率 |'

    def constitution(self):
        return '|:--|:--|:--|:--:|'

    def generate_row(self, malware):
        return '| [' + malware.file_name +  '](' + malware.permalink + ') |'+ malware.file_type  + '|' + malware.datetime + '|' + malware.detection_rate + '|'

class VirusTotal():
    VIRUS_TOTAL_REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'
    def __init__(self):
        self.set_api_key()
        self.request_time = 0

    def request(self, malware):
        parameters = {'resource': malware.sha256, 'apikey': self.api_key}
        data = urllib.urlencode(parameters)
        request = urllib2.Request(self.VIRUS_TOTAL_REPORT_URL, data)
        response = urllib2.urlopen(request)
        res_json = json.loads(response.read())
        self.increment_request_time()

        if res_json['response_code'] == 0:
            print '[LOG] RESPONSE CODE IS 0.'
            print res_json
        malware.set_permalink(res_json)
        malware.set_detection_rate(res_json)
#        malware.set_file_kind(res_json)

    def increment_request_time(self):
        self.request_time+=1

    def check_request_time(self):
        return self.request_time != 0 and self.request_time % 4 == 0

    # read api_key from ./api_key.txt
    def set_api_key(self):
        api_key_file_path = './api_key.txt'
        with open(api_key_file_path) as f:
          read = f.read()
        self.api_key = read.replace('\n', '')
        print '[LOG] api key: ' + self.api_key

main()

