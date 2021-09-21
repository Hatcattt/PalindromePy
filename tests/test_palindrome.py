import unittest
from ..palindrome import normalize
from ..palindrome import is_palindrome


class TestPalindromePy(unittest.TestCase):
    # TESTING NORMALIZE FUNCTION
    def test_normalise_a_sentence(self):
        result = normalize("Hello World !")
        self.assertEqual("helloworld", result)

    def test_normalise_a_sentence2(self):
        result = normalize("Hello world, it's me again !")
        self.assertEqual("helloworlditsmeagain", result)

    def test_normalise_a_sentence_with_space(self):
        result = normalize("  ,  ")
        self.assertEqual("", result)

    # TESTING IS_PALINDROME FUNCTION
    def test_simple_palindrome(self):
        result = is_palindrome("kayak")
        self.assertTrue(result)

    def test_bad_simple_palindrome(self):
        result = is_palindrome("hello")
        self.assertFalse(result)

    def test_complex_palindrome(self):
        result = is_palindrome("No, it is open on one position.")
        self.assertTrue(result)

    def test_bad_complex_palindrome(self):
        result = is_palindrome("I am a palindrome !")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
