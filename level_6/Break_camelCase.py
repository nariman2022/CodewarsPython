Complete the solution so that the function will break up camel casing, using a space between words.
Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

def solution(s):
    if not s:
        return s

    res = s[0]
    for char in s[1:]:
        if char.isupper():
            res += ' ' + char
        else:
            res += char
    return res
