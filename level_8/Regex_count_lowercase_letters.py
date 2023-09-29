#Your task is simply to count the total number of lowercase letters in a string.

import re
def lowercase_count(strng):
    x = re.findall('[a-z]', strng)
    return len(x)