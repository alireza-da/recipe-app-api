from django.test import TestCase
from calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtracts_numbers(self):
        # test value subtracted and returned
        self.assertEqual(subtract(5, 11), 6)
