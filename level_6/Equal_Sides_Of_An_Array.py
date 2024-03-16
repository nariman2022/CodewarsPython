# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the
# integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make
# this happen, return -1.
# Input
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
#
# Output
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index
# that fits these rules, then you will return -1.
#
# Note
# If you are given an array with multiple answers, return the lowest correct index.

def find_even_index(arr):
    for n in range(len(arr)):
        if sum(arr[:n]) == sum(arr[n+1:]):
            return n
    return -1