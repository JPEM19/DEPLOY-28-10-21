"""
String to know if it is a palindrome
"""


def check(word):
    if (word==word[::-1]):
        return "palindrome"
    else :
        return "not palindrome"
