import unittest

from lab10.math import (
    factorial,
    conversion)


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(1814400, factorial.factorial(10))


class TestConversion(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual(2, conversion.decimal_to_binary('2'))

    def test_bin_to_dec(self):
        self.assertEqual('1111110010', conversion.binary_to_decimal(1010))

    def test_dec_to_hex(self):
        self.assertEqual('A', conversion.hex_to_decimal(10))

    def test_hex_to_dex(self):
        self.assertEqual(48, conversion.decimal_to_hex('30'))


if __name__ == '__main__':
    unittest.main()
