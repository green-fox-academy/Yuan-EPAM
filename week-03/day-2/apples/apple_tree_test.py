from apple_tree import AppleTree
import unittest

class TestAppleTree(unittest.TestCase):
    def test_get(self):
        apple_tree = AppleTree()
        # self.assertEqual(apple_tree.apple, 'apple')
        self.assertEquals(apple_tree.apple, 'apples')


if __name__=='__main__':
    unittest.main()