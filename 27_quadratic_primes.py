#!/usr/bin/python

# Euler discovered the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
# by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

# First, get some primes(sieve of Eratosthenes)
def precompute_primes(limit, primes):
    sieve = [True] * limit
    sieve[0] = False  # 1 is not prime
    sum = 0
    curr = 1
    while curr < limit:
        # find next prime by skipping False in the sieve
        while curr <= limit and sieve[curr - 1] == False:
            curr += 1
        if curr > limit:
            break  # the end
        sieve[curr - 1::curr] = [False] * (limit / curr)
        primes.add(curr)

limit = 1000
primes = set()
precompute_primes(2 * limit * limit, primes)
print 'num precomputed primes:', len(primes)

def func(a, b, n):
    return n * n + a * n + b

def num_yielded_primes(func):
    for i in xrange(limit):
        f = func(i)
        if f not in primes:
            return i

max_num_yielded = 0
for a in xrange(-999, 1000):
    for b in [i for i in primes if i < 1000]:
        f = lambda x: x * x + a * x + b
        num_yielded = num_yielded_primes(f)
        if num_yielded > max_num_yielded:
            print 'for a =', a, 'b =', b, 'num of yielded primes:', num_yielded
            max_num_yielded = num_yielded
            res = a * b

print 'result:', res
