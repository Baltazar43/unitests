import unittest

from example import check_palindrome

class Test_check_palindrome (unittest.TestCase):
    def test_first (self):
        self.assertEqual(check_palindrome("radar"), True)
    def test_two (self):
        self.assertEqual(check_palindrome("ad"), False)
    def test_three (self):
        self.assertEqual(check_palindrome("22"), True)