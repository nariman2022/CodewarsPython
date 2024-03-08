# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    res = []
    for digit in (str(n))[::-1]:
        res.append(int(digit))
    return res

    #return [int(digit) for digit in reversed(str(n))]