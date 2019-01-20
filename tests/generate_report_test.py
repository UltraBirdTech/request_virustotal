from unittest import TestCase
from generate_report import Cowrie

class TestCowrie(TestCase):
  def test_first_char(self):
    cowrie = Cowrie()
    self.assertEqual(cowrie.first_char(), 'c')
