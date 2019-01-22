# [USAGE]: python -m unittest tests/generate_report_test.py
import unittest
from generate_report import Cowrie
from generate_report import Dionaea
from unittest import mock

class TestCowrie(unittest.TestCase):
  def setUp(self):
    self.cowrie = Cowrie()

  def test_init_path(self):
    self.assertEqual(self.cowrie.path, './cowrie/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.cowrie.first_char(), 'c')

  @unittest.skip("I should create mock and reseponse from Mock")
  def test_file_name(self):
    pass
    # Mock 使用してdatetime.now()の挙動を同じにする。
    self.assertEqual(self.cowrie.file_name(), 'something write.')

  def test_class_name(self):
    self.assertEqual(self.cowrie.class_name(), 'Cowrie')

class TestDionaea(unittest.TestCase):
  def setUp(self):
    self.cowrie = Dionaea()

  def test_init_path(self):
    self.assertEqual(self.cowrie.path, './dionaea/downloads/malware/')

  def test_first_char(self):
    self.assertEqual(self.cowrie.first_char(), 'c')

  @unittest.skip("I should create mock and reseponse from Mock")
  def test_file_name(self):
    pass
    # Mock 使用してdatetime.now()の挙動を同じにする。
    self.assertEqual(self.cowrie.file_name(), 'something write.')

  def test_class_name(self):
    self.assertEqual(self.dionaea.class_name(), 'Dionaea')
