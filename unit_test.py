import unittest
from word_checker import WordChecker

class TestWordChecker(unittest.TestCase):
    def test_method_one(self):
        word_checker = WordChecker("Emeka") ## Ensuring palindrome works
        another_word_checker = WordChecker("Ada") ##testing for case sensitivity too
        assert word_checker.is_word_palindrome(1) == False,"Should be false as Emeka is not a palindrome"
        assert another_word_checker.is_word_palindrome(1) == True,"Should be True as Ada is a palindrome"

    def test_method_two(self):
        word_checker = WordChecker("Emeka") ## Ensuring palindrome works
        another_word_checker = WordChecker("Ada") ##testing for case sensitivity too
        assert word_checker.is_word_palindrome(2) == False,"Should be false as Emeka is not a palindrome"
        assert another_word_checker.is_word_palindrome(2) == True,"Should be True as Ada is a palindrome"

if __name__ == "__main__":
    unittest.main()