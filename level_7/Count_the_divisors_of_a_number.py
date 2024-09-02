# Count the number of divisors of a positive integer n.
# Random tests go up to n = 500000, but fixed tests go higher.
#
# Examples (input --> output)
# 4 --> 3 // we have 3 divisors - 1, 2 and 4
# 5 --> 2 // we have 2 divisors - 1 and 5
# 12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
# 30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30


def divisors(n):
        res = [1]
        for i in range(1, n):
            if n % i == 0:
                res.append(i)
        return len(res)

def divisors(n):
    return len(list(i for i in range(1, n) if n % i == 0)) + 1

def divisors(n):
    return len(list(x for x in range (1, n+1) if n % x == 0))

