import unittest

from leetcode_python.algorithms.strings import valid_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Test for the file valid_palindrome.py
    """

    def test_isPalindrome(self):
        self.assertTrue(isPalindrome('racecar'))
        self.assertFalse(isPalindrome('bass'))