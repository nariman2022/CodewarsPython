# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text = text.split()
    res = []
    for word in text:
        if word.isalpha():
            res.append(word[1:]+ word[0]+'ay')
        else:
            res.append(word)
    return ' '.join(res)