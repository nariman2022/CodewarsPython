#For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example
# below. Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes
# from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    return ' '.join(x[0].upper() + x[1:].lower() for x in string.split())
