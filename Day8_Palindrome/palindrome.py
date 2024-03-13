"""
Impliment a function that checks whether a given string is a plalindrome.

A Palindrome is a word, phrase, number, or other sequence of characters that reads the same
forward as backwards (ignoring spaces, punctuation, and capitalization).

Your function should return True if the input string is a palindrome and False otherwise.

_______________________
Python makes this process rather easy due to it's method reversed(), which when
input into a list, supplies reversed duplicate of a list. 

This coupled with Python's default ability to iterate through a string, means that
this is an incredbily simple process
"""


def palindrome_checker(user_input=input("Input a String: ")):
    new_input = list(user_input.lower().replace(" ", "").strip(".,"))
    print(new_input)
    reversed_input = list(reversed(new_input))
    print(reversed_input)
    print(new_input == reversed_input)


palindrome_checker()
