# The number has been mixed up with the text. Your goal is to retrieve the number from the text,
# can you return the number back to its original state?
# Your task is to return a number from a string.
# You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in the order they occur.

def filter_string(string):
    num = []
    #     for x in string:
    #         if x.isdigit():
    #             num.append(x)
    return int(''.join(x for x in string if x.isdigit()))