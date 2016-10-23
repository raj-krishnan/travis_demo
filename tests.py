import gcd
import unittest


class TestGCD(unittest.TestCase):

    def test_co_prime_numbers(self):
        self.assertEqual(gcd.gcd(40, 39), 1)
        self.assertEqual(gcd.gcd(7, 13), 1)

    def test_non_co_prime_numbers(self):
        self.assertEqual(gcd.gcd(40, 30), 10)
        self.assertEqual(gcd.gcd(64, 48), 16)
