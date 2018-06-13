import unittest

import xmlrunner

from lab10.strings import (
    anagram,
    palindrome)


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.is_anagram('ant', ['tan', 'stand', 'at', 'nat']), ['tan', 'nat'])


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome.is_palindrome('madam'))
        self.assertFalse(palindrome.is_palindrome('eleven'))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
