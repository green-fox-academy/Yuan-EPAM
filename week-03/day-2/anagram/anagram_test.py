import anagram
import unittest

class TestAnagramMethod(unittest.TestCase):
    def test_anagram_no_duplicated(self):
        str1 = 'abcd'
        str2 = 'bdca'
        actual = anagram.if_anagram(str1, str2)
        expected = True
        self.assertEqual(actual, expected)

    def test_anagram_duplicated(self):
        str1 = 'aaabbcdd'
        str2 = 'bcdbdaaa'
        actual = anagram.if_anagram(str1, str2)
        expected = True
        self.assertEqual(actual, expected)

if __name__=="__main__":
    unittest.main()