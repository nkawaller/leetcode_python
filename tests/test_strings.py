from algorithms.strings import is_palindrome

import unittest

class TestIsPalindrome(unittest.TestCase):
    """
    Test for the file valid_palindrome.py
    """

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('A man a plan a canal: Panama'))
        self.assertFalse(is_palindrome('Race a car'))


if __name__ == '__main__':
    unittest.main()