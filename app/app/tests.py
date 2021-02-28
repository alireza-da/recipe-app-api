from django.test import TestCase

import app.app.calc as calc


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(calc.add(3, 8), 11)
