#Implement String #digit , which should return true if given object is a digit (0-9), false otherwise.

import re

def is_digit(n):
    x = re.fullmatch('^\d$', n)
    return bool(x)