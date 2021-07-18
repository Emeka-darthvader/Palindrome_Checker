

class WordChecker():
    def __init__(self,word):
        self.word = word.lower() ## ensuring we make all words lower case
    
    def is_word_palindrome(self,method):
        if (method == 1):
            reversed_word = self.word[::-1]
            if (self.word == reversed_word):
                return True
            else:
                return False
        elif (method==2):
            length_of_word = len(self.word)
            reversed_word = ""
            for i in reversed(range(length_of_word)):
                reversed_word += self.word[i]
            if (self.word == reversed_word):
                return True
            else:
                return False


word = "refers"
word_checker = WordChecker(word)

''' methods for checking palindrome: 1, 2'''

if (word_checker.is_word_palindrome(2)):
    print ("The word is a palindrome")
else:
    print("This word is not a palindrome")

