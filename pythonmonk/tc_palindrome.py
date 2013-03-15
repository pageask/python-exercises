import unittest
from palindrome import CustomString


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palindrome = CustomString("Never odd or even")
        self.no_palindrome = CustomString("How are you?")

    def tearDown(self):
        pass

    def test_palindrome(self):
        self.assertEqual(True, self.palindrome.palindrome())
        self.assertEqual(False, self.no_palindrome.palindrome())


if __name__ == "__main__":
    unittest.main()
