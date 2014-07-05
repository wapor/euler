#!/usr/bin/python

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

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

def are_permutations(x, y, z):
    return sorted(str(x)) == sorted(str(y)) and sorted(str(y)) == sorted(str(z))

first = 1000
last = 9999

primes = []
precompute_primes(last + 1, primes)
primes = [i for i in primes if i >= first]
primes_set = set(primes)

for i in xrange(0, len(primes) - 2):
    x = primes[i]
    for j in xrange(i + 1, len(primes) - 1):
        y = primes[j]
        z = y + y - x
        if z in primes_set and are_permutations(x, y, z):
            print 'Result:', x, y, z
        
