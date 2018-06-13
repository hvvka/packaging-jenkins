import unittest

import xmlrunner

from lab10.math import (
    factorial,
    conversion)


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial.factorial(10), 3628800)


class TestConversion(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual('10', conversion.decimal_to_binary(2))

    def test_bin_to_dec(self):
        self.assertEqual(10, conversion.binary_to_decimal('1010'))

    def test_dec_to_hex(self):
        self.assertEqual('1E', conversion.decimal_to_hex(30))

    def test_hex_to_dex(self):
        self.assertEqual(30, conversion.hex_to_decimal('1E'))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
