#!/usr/bin/python

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

def factorial(x):
    assert x >= 0
    f = 1
    for i in xrange(1, x + 1):
        f *= i
    return f


def get_perm(num, size):
    assert num <= factorial(size)

    perm_from = range(size)
    perm_to = []

    num -= 1
    for i in xrange(size, 1, -1):
        f = factorial(i - 1)
        chosen = num / f
        perm_to.append(perm_from[chosen])
        del perm_from[chosen]
        num %= f
    assert len(perm_from) == 1
    perm_to.append(perm_from[0])
    return perm_to
        
# for i in xrange(1, 25):
#     print i, get_perm(i, 4)

print get_perm(1000000, 10)






