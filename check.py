#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import hashlib
import json
import os
import subprocess
import sys
import urllib
import urllib2
from datetime import datetime
from datetime import timedelta
from time import sleep

MALWARE_DIR = './downloads/malware/'

################################
# main method
def main():
    print '[LOG] START SCRIPT'
    argv = Argv()
    file_array = sorted(glob.glob( MALWARE_DIR + '*'), key=os.path.getmtime)
    print '[LOG] target file num is :' + str(len(file_array))
    malwares = []
    virus_total = VirusTotal()
    for file in file_array:
       with open(file, 'rb') as f:
           malware = MalwareFile(f)

       if not malware.check_date(argv.argument_date):
           print '[LOG] Skip: ' + malware.file_name
           continue

       if virus_total.check_request_time():
           print '[LOG] Sleep 65 seconds.'
           sleep(65) # APIに1分間における使用回数があるため60秒近くsleepする

       print '[LOG] Check: ' + malware.file_name
       virus_total.request(malware)
       malwares.append(malware)

    output_file = OutputFile()
    output_file.generate(malwares)
    print '[LOG] END SCRIPT'

################################
# argv class
class Argv:
    DEFAULT_DATE = 7
    def __init__(self):
      self.argv = sys.argv
      self.set_check_date()

    def set_check_date(self):
        if (len(self.argv) != 2):
            print 'argument date is nothing so, set default date:' + str(self.DEFAULT_DATE)
            self.argument_date = self.DEFAULT_DATE
            return

        self.argument_date = self.argv[1]
            
#################################
# マルウェアクラス
# __init__() f: file information
class MalwareFile:
    FILE_NAME_LIMIT = 10
    def __init__(self, f):
        self.set_file_name(f)
        self.set_sha_256(f)
        self.set_datetime()
        self.set_file_type()
        self.kind = '-'

    def set_file_name(self, f):
        self.file_name = f.name.split('/')[-1]
        if self.FILE_NAME_LIMIT < len(self.file_name):
          # file name is long. So, add limit and slice.
          self.display_file_name = self.file_name[0:9] + '...'
          return

        self.display_file_name = self.file_name

    def set_sha_256(self, f):
        self.sha256 = hashlib.sha256(f.read()).hexdigest()

    def set_datetime(self):
        time_float = os.path.getmtime( MALWARE_DIR + self.file_name )
        self.datetime = datetime.fromtimestamp(time_float).strftime('%Y/%m/%d %H:%M:%S')

    # 自分自身のファイルタイプを調査し格納する。
    # 内部的に Linux の file コマンドを打ち結果を格納する。
    def set_file_type(self):
        proc = subprocess.Popen('file ' + MALWARE_DIR + self.file_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        file_type = proc.stdout.readline()
        proc.poll()
        file_type_split = file_type.split(':')[-1]
        self.file_type = file_type_split.split(',')[0].replace('\n', '')

    # virus total へのURLを格納する。
    # ステータスコードが0の場合、'permalink'のハッシュキーは存在しないためエラーになる。
    # エラーになる前に、キーの存在チェックを行いエラーを回避。
    def set_permalink(self, data):
        self.permalink = data['permalink'] if ('permalink' in data) else '-'

    # virus total の検出率を格納する。
    # ステータスコードが0の場合、'positives', 'total' のハッシュキーは存在しないためエラーになる。
    # エラーになる前に、キーの存在チェックを行いエラーを回避。
    def set_detection_rate(self, data):
        self.detection_rate = str(data['positives']) + '/' + str(data['total']) if ('positives' in data) else '-'

    # ファイルの日付が、検査対象の日付に含まれているかの確認。
    def check_date(self, date):
        week_ago_date = datetime.now().date() + timedelta(days=-int(date)) # change here.
        file_date = datetime.strptime(self.datetime,'%Y/%m/%d %H:%M:%S').date()
        return week_ago_date <= file_date

####################################
# Output File Class
# generate output file for paste a article.
class OutputFile:
    def generate(self, malwares):
        length = len(malwares)
        if length == 0:
            print '[LOG] Not Create file: check file num equal zero.'
            return

        with open(self.generate_file_name(), 'w') as f:
            f.writelines('Total: ' + str(length) + '\n')
            f.writelines('\n')
            f.writelines(self.header() + '\n')
            f.writelines(self.constitution() + '\n')
            for malware in malwares:
                f.writelines(self.generate_row(malware) + '\n')

    def generate_file_name(self):
        # like 'virus_total_20180000000000.txt'
        return 'virus_total_' + str(datetime.now().strftime('%Y%m%d%H%M%S')) + '.txt'

    def header(self):
        return '| ファイル名 | 取得日時 | タイプ| 検出率 |'

    def constitution(self):
        return '|:--|:--|:--|:--:|'

    def generate_row(self, malware):
        return '| [' + malware.display_file_name +  '](' + malware.permalink + ') |'+ malware.datetime  + '|' + malware.file_type + '|' + malware.detection_rate + '|'

    def file_constitution(self):
        # something write...
        # I want to automatic.
        print 'something write'

####################################
# Virus Totalに関するClass
class VirusTotal():
    VIRUS_TOTAL_REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'
    DEFAULT_REQUEST_TIME = 0
    API_LIMIT_TIME = 4
    def __init__(self):
        self.set_api_key()
        self.request_time = self.DEFAULT_REQUEST_TIME

    # Virus Totalへ実際にリクエストをするメソッド
    def request(self, malware):
        parameters = {'resource': malware.sha256, 'apikey': self.api_key}
        data = urllib.urlencode(parameters)
        request = urllib2.Request(self.VIRUS_TOTAL_REPORT_URL, data)
        response = urllib2.urlopen(request)
        res_json = json.loads(response.read())
        self.increment_request_time()

        # add error hudling about error from api
        if res_json['response_code'] == 0:
            print '[LOG] RESPONSE CODE IS 0.'
            print res_json

        malware.set_permalink(res_json)
        malware.set_detection_rate(res_json)

    # Virus Totalへのリクエスト回数を計算するメソッド
    def increment_request_time(self):
        self.request_time+=1

    # Virus Total へのリクエスト回数をチェックするメソッド
    # NOTE: virus totalのAPIは1分間に4回までしか使用することができない
    def check_request_time(self):
        return (self.request_time != 0) and ((self.request_time % self.API_LIMIT_TIME) == 0)

    # read api_key from ./api_key.txt
    def set_api_key(self):
        api_key_file_path = './api_key.txt'
        with open(api_key_file_path) as f:
          read = f.read()
        self.api_key = read.replace('\n', '')
        print '[LOG] api key: ' + self.api_key

main()

