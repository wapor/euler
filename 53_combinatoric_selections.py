#!/usr/bin/python

# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# C(n,r) = n!/r!(n-r)!
# where r <= n
# It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)
    
@memoize
def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x - 1)

def num_combinations(n, r):
    assert n >= r
    assert r > 0
    return  fact(n) / (fact(r) * fact(n-r))


limit = 100
count = 0
for n in xrange(1, limit + 1):
    for r in xrange(1, n + 1):
        if num_combinations(n, r) > 1000000:
            count += 1
print count
        
