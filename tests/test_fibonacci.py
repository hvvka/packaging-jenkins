"""
Test for Fibonacci implementations logic.
"""

import unittest

import xmlrunner

from lab10.fibonacci import recursion


class TestFibonacciImplementations(unittest.TestCase):
    """
    Tests for Fibonacci recursion.
    """

    def test_implementations_same_result(self):
        """
        Verify results.
        """

        result = getattr(recursion, 'get_sequence')(0)
        self.assertEqual([0], result)

        result = getattr(recursion, 'get_sequence')(1)
        self.assertEqual([0, 1], result)

        result = getattr(recursion, 'get_sequence')(10)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], result)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
