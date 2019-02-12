# [USAGE]: python -m unittest tests/generate_report_test.py
import unittest
import freezegun
import sys, os
from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock
from generate_report import Argv
from generate_report import OutputFile
from generate_report import VirusTotal
from generate_report import Cowrie
from generate_report import Dionaea
from generate_report import MalwareFile
from generate_report import MyException

class MockMalware:
  def __init__(self):
    self.display_file_name = 'test_file_name'

class MockFile: def __init__(self): self.file_name = 'FILE_NAME'

class TestArgv(unittest.TestCase):
  def setUp(self):
    del sys.argv[0]
    sys.argv.append('c')
    self.argv = Argv()
    self.argv.argv = ['file_name', 'c', 7]

  def test_set_kind_honey(self):
    self.argv.set_kind_of_honey()
    self.assertEqual(type(self.argv.honey), type(Cowrie()))

    self.argv.argv[1] = 'd'
    self.argv.set_kind_of_honey()
    self.assertEqual(type(self.argv.honey), type(Dionaea()))

    self.argv.argv[1] = 'A'
    with self.assertRaises(MyException):
      self.argv.set_kind_of_honey() # 存在しない文字列が入った場合はErrorとする

    # 引数が存在しない場合はデフォルトの 'c' が入る
    self.argv.argv[1:3] = []
    self.argv.set_kind_of_honey()
    self.assertEqual(type(self.argv.honey), type(Cowrie()))

  def test_set_check_date(self):
    self.argv.set_check_date()
    self.assertEqual(self.argv.argument_date, 7)

    self.argv.argv[2] = 5
    self.argv.set_check_date()
    self.assertEqual(self.argv.argument_date, 5 )

    self.argv.argv[2] = 'A'
    with self.assertRaises(MyException):
      self.argv.set_check_date()

    # 引数が存在しない場合はデフォルトの 7 が入る
    self.argv.argv[1:3] = []
    self.argv.set_check_date()
    self.assertEqual(self.argv.argument_date, 7 )

class TestMalwareFile(unittest.TestCase):
  def setUp(self):
    self.malware_mock.sha256 = MagicMock(return_value='sha256')
    self.malware_mock.set_permalink = MagicMock(return_value='permalink')
    self.malware_mock.set_detection_rate = MagicMock(return_value='detection_rate')

  def test_set_file_name(self):
    # write something.

  def test_set_sha_256(self):
    # write something.

class TestOutputFile(unittest.TestCase):
  def setUp(self):
    self.malware_mock = MockMalware()
    self.malware_mocks = [self.malware_mock]
    self.output_file = OutputFile()

  @freezegun.freeze_time('2019-01-01')
  def test_generate_file_name(self):
    # freezegun を使用して2019-01-01に固定
    self.assertEqual(self.output_file.generate_file_name(Cowrie()), 'cowrie_virus_total_20190101000000.txt')
    self.assertEqual(self.output_file.generate_file_name(Dionaea()), 'dionaea_virus_total_20190101000000.txt')

  def test_header(self):
    self.assertEqual(self.output_file.header(), '|ファイル名|取得日時|タイプ|検出率|')

  def test_consititution(self):
    self.assertEqual(self.output_file.constitution(), '|:--|:--|:--|:--:|')

  # Malware Mock file
  @unittest.skip('Should create a mock about URL request')
  def test_generation_row(self):
    skip
    self.assertEqual(self.output_file.constitution(), '|:--|:--|:--|:--:|')

class TestVirusTotal(unittest.TestCase):
  def setUp(self):
    self.virus_total = VirusTotal()
    # setting malware mock
    self.malware_mock = MockMalware()
    self.malware_mock.sha256 = MagicMock(return_value='sha256')
    self.malware_mock.set_permalink = MagicMock(return_value='permalink')
    self.malware_mock.set_detection_rate = MagicMock(return_value='detection_rate')

  def test_init_values(self):
    self.assertEqual(self.virus_total.VIRUS_TOTAL_REPORT_URL, 'https://www.virustotal.com/vtapi/v2/file/report')
    self.assertEqual(self.virus_total.DEFAULT_REQUEST_TIME, 0)
    self.assertEqual(self.virus_total.API_LIMIT_TIME, 4)
    self.assertEqual(self.virus_total.api_key[0:5], 'e7416') # セキュリティの都合上APIキー全てを出さずに最初の5文字を確認する

  @unittest.skip('Should create a mock about URL request')
  def test_request(self):
    self.assertEqual(self.virus_total.request_time, 0)
#    with unittest.patch('json.loads') as json_mock:
#      json = json_mock.return_value
#      json.loads.return_value = 'value'
#      self.virus_total.request(self.malware_mock)

    skip
    self.assertEqual(self.virus_total.request_time, 1)
    
  def test_increment_request_time(self):
    self.assertEqual(self.virus_total.request_time, 0)
    self.virus_total.increment_request_time()
    self.assertEqual(self.virus_total.request_time, 1)

  # check_request_timeは計算結果が4の倍数の場合のみTrueを返却する
  def test_check_request_time(self):
    # 初期値は0のためFalseが返却される
    self.assertFalse(self.virus_total.check_request_time())

    # リクエスト回数が1の場合はFlase
    self.virus_total.request_time = 1
    self.assertFalse(self.virus_total.check_request_time())

    # リクエスト回数が4の場合はTrue
    self.virus_total.request_time = 4
    self.assertTrue(self.virus_total.check_request_time())

    # リクエスト回数が5以上で4で割り切れない数の場合Flase
    self.virus_total.request_time = 5
    self.assertFalse(self.virus_total.check_request_time())

    # リクエスト回数が5以上で4で割り切れる数の場合True
    self.virus_total.request_time = 8
    self.assertTrue(self.virus_total.check_request_time())

class TestCowrie(unittest.TestCase):
  def setUp(self):
    self.cowrie = Cowrie()

  def test_init_path(self):
    self.assertEqual(self.cowrie.path, './cowrie/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.cowrie.first_char(), 'c')

  @freezegun.freeze_time('2019-01-01')
  def test_file_name(self):
    self.assertEqual(self.cowrie.file_name(), 'cowrie_virus_total_20190101000000.txt') # freezegun を使用して2019-01-01に固定

  def test_class_name(self):
    self.assertEqual(self.cowrie.class_name(), 'Cowrie')

class TestDionaea(unittest.TestCase):
  def setUp(self):
    self.dionaea = Dionaea()

  def test_init_path(self):
    self.assertEqual(self.dionaea.path, './dionaea/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.dionaea.first_char(), 'd')

  @freezegun.freeze_time('2019-01-01')
  def test_file_name(self):
    self.assertEqual(self.dionaea.file_name(), 'dionaea_virus_total_20190101000000.txt') # freezegun を使用して2019-01-01に固定

  def test_class_name(self):
    self.assertEqual(self.dionaea.class_name(), 'Dionaea')
