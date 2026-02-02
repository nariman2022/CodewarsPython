# Complete the method which accepts an array of integers, and returns one of the following:
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return f"yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return f"yes, descending"
    else:
        return "no"