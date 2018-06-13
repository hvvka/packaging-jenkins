import unittest
import random

import xmlrunner

from lab10.sorting import bubble_sort


class TestSortingAlgorithm(unittest.TestCase):
    def setUp(self):
        # to test numbers
        self.array = list(range(15))
        random.shuffle(self.array)
        self.sorted_array = list(range(15))

        # to test alphabets
        string = 'pythonisawesome'
        self.alphaArray = list(string)
        random.shuffle(self.alphaArray)
        self.sorted_alpha_array = sorted(string)


class TestBubbleSort(TestSortingAlgorithm):
    def test_bubble_sort(self):
        self.result = bubble_sort.sort(self.array)
        self.assertEqual(self.result, self.sorted_array)

        self.alphaResult = bubble_sort.sort(self.alphaArray)
        self.assertEqual(self.alphaResult, self.sorted_alpha_array)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
