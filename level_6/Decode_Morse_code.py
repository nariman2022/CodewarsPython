The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded
as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally
capital letters are used. When the message is written in Morse code, a single space is used
to separate the character codes and 3 spaces are used to separate words. For example,
the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    a = ''
    z = morse_code.split(' ')
    for i in z:
        if i == '':
            a += ' '
        else:
            a += MORSE_CODE[i]
    return a.replace('  ', ' ').strip()