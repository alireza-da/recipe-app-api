from django.test import TestCase

from app.app.calc import add


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)
