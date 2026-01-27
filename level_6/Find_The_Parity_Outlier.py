You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for
a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(int):
    odd_list = []
    even_list = []
    for n in int:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)
    return even_list.pop() if len(even_list) < len(odd_list) else odd_list.pop()