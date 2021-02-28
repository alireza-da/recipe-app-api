from django.test import TestCase
import calc


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(calc.add(3, 8), 11)
