import os
import sys

from django.test import TestCase

from calc import add

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)
