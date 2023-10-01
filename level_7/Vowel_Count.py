# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(sen):
    return sum(x in 'aeiou' for x in sen)

def get_count(sen):
    return len(list(filter(lambda x: x in 'aeiou', sen)))