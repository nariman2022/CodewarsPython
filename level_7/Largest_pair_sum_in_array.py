# Given a sequence of numbers, find the largest pair sum in the sequence.

def largest_pair_sum(numbers):
    return sum(sorted(numbers)[-2::])