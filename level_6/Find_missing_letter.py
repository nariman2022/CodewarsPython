Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
in the array. You will always get an valid array. And it will be always exactly one letter be missing. The length of
the array will always be at least 2.
The array will always contain letters in only one case.
Example:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

from string import ascii_letters

def find_missing_letter(chars):
    start = ascii_letters.index(chars[0])
    for char in ascii_letters[start:]:
        if char not in chars:
            return char


def find_missing_letter(chars):
    start = ascii_letters.index(chars[0])
    return next(char for char in ascii_letters[start:] if char not in chars)