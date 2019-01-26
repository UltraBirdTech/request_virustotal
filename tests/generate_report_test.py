# [USAGE]: python -m unittest tests/generate_report_test.py
import unittest
import freezegun
from datetime import datetime
from unittest import mock
from generate_report import VirusTotal
from generate_report import Cowrie
from generate_report import Dionaea

class TestVirusTotal(unittest.TestCase):
  def setUp(self):
    self.virus_total = VirusTotal()

  def test_init_values(self):
    self.assertEqual(self.virus_total.VIRUS_TOTAL_REPORT_URL, 'https://www.virustotal.com/vtapi/v2/file/report')
    self.assertEqual(self.virus_total.DEFAULT_REQUEST_TIME, 0)
    self.assertEqual(self.virus_total.API_LIMIT_TIME, 4)



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
