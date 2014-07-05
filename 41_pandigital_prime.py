#!/usr/bin/python

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?

import itertools
sieve = []

def get_primes(limit):
    global sieve
    sieve = [True] * limit
    sieve[0] = False  # 1 is not prime
    curr = 1
    while curr < limit:
        # find next prime by skipping False in the sieve
        while curr <= limit and sieve[curr - 1] == False:
            curr += 1
        if curr > limit:
            break  # the end
        sieve[curr - 1::curr] = [False] * (limit / curr)
        sieve[curr - 1] = True
        curr += 1

# There are no pandigital primes of len 8 or 9 since
# sum(range(1, 10)) % 3 == 0 and sum(range(1, 9)) % 3 == 0
get_primes(10 * 1000 * 1000)
print sieve[0:20]


for digits in range(1, 9):
    print 'checking %d-pandigital numbers' % (digits - 1)
    for i in itertools.permutations(xrange(1, digits)):
        num = 0
        for j in i:
            num = num * 10 + j
        if sieve[num - 1]:
            print num
