from sum import Sum
import unittest

class TestSum(unittest.TestCase):
    def test_sum_positive(self):
        nums = [1, 2, 3, 4]
        actual = Sum(nums).get_sum()
        expected = 10
        self.assertEqual(actual, expected)
        self.assertEqual(actual, expected)

    def test_sum_negative(self):
        nums = [-1, -2, -3]
        actual = Sum(nums).get_sum()
        expected = -6
        self.assertEqual(actual, expected)

    def test_sum_empty(self):
        num = []
        actual = Sum(num).get_sum()
        expected = 0
        self.assertEqual(actual, expected)

    def test_sum_single(self):
        num = [1]
        actual = Sum(num).get_sum()
        expected = 1
        self.assertEqual(actual, expected)

    def test_sum_positive_with_None(self):
        nums = [1, 2, None, 4]
        actual = Sum(nums).get_sum()
        expected = 7
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()