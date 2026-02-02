# Write a function that takes a positive integer n,
# sums all the cubed values from 1 to n (inclusive), and returns that sum.

def sum_cubes(n):
    return sum([d ** 3 for d in range(n+1)])