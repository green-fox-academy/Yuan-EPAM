import unittest
from extension import add, max_of_three, median, is_vovel, translate

class TestExtend(unittest.TestCase):
    def test_add_2_and_3_is_5(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_1_and_4_is_5(self):
        self.assertEqual(add(1, 4), 5)

    def test_add_5_and_10(self):
        self.assertEqual(add(5, 10), 15)

    def test_max_of_three_first(self):
        self.assertEqual(max_of_three(5, 4, 10), 10)

    def test_max_of_three_third(self):
        self.assertEqual(max_of_three(3, 4, 5), 5)

    def test_median_empty(self):
        self.assertEqual(median([]), None)

    def test_median_four(self):
        self.assertEqual(median([7, 5, 3, 5]), 5)

    def test_median_five(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(translate('lagopus'), 'lavagovopuvus')

    def test_translate_empty(self):
        self.assertEqual(translate([]), '')

if __name__ == '__main__':
    unittest.main()
