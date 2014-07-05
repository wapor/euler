#!/usr/bin/python

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math

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
        primes.append(curr)

def is_circular_prime(num, primes):
    x = 10
    y = 10 ** int(math.log10(num))
    while y >= 10:
        left, right = divmod(num, x)
        rotated = right * y + left
        if rotated not in primes:
            return False 
        y /= 10
        x *= 10
    print num
    return True
        
limit = 1000 * 1000
primes = []

precompute_primes(limit, primes)
set_primes = set(primes)

num = 0
for i in set_primes:
    if is_circular_prime(i, set_primes):
        num += 1

print 'result:', num
