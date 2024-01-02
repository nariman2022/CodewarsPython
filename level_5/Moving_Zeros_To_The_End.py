# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of
# the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    lst1 = []
    lst2 = []
    for digit in lst:
        if digit != 0:
            lst1.append(digit)
        else:
            lst2.append(digit)
    return lst1 + lst2
