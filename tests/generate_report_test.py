# [USAGE]: python -m unittest tests/generate_report_test.py
import unittest
#import datetime
#from datetime import date
import freezegun
from datetime import datetime
from unittest import mock
from generate_report import Cowrie
from generate_report import Dionaea

#fake_date = datetime.datetime(2018,1,1)
#with mock.patch('datetime.datetime') as dt:
#  dt.now.return_value = fake_date
#  from datetime import datetime
#  datetime.now()

#with mock.patch('datetime.datetime') as mock_date:
#  mock_date.now.return_value = datetime.datetime(2018,1,1)
  
class TestCowrie(unittest.TestCase):
  def setUp(self):
    self.cowrie = Cowrie()

  def test_init_path(self):
    self.assertEqual(self.cowrie.path, './cowrie/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.cowrie.first_char(), 'c')

#  @unittest.skip("I should create mock and reseponse from Mock")
#  @mock.patch('datetime.datetime')
  @freezegun.freeze_time('2018-01-01')
  def test_file_name(self):
    print(datetime.now())
#    datetime_now.return_value = datetime.now()
    # Mock 使用してdatetime.now()の挙動を同じにする。
    self.assertEqual(self.cowrie.file_name(), 'cowrie_virus_total_20180101000000.txt')

  def test_class_name(self):
    self.assertEqual(self.cowrie.class_name(), 'Cowrie')

class TestDionaea(unittest.TestCase):
  def setUp(self):
    self.dionaea = Dionaea()

  def test_init_path(self):
    self.assertEqual(self.dionaea.path, './dionaea/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.dionaea.first_char(), 'd')

  @unittest.skip("I should create mock and reseponse from Mock")
  def test_file_name(self):
    pass
    # Mock 使用してdatetime.now()の挙動を同じにする。
    self.assertEqual(self.cowrie.file_name(), self.dionaea.class_name() + 'virus_total')

  def test_class_name(self):
    self.assertEqual(self.dionaea.class_name(), 'Dionaea')
