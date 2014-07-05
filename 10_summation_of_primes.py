#!/usr/bin/python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

# brutforce
primes = [2, 3]

limit = 2000000
candidate = 3
while primes[-1] < limit:
    candidate += 2
    sq = math.sqrt(candidate)
    found = False
    for prime in primes:
        if candidate % prime == 0:
            found = True
            break
        if prime > sq:
            found = False
            break
    if not found:
        primes.append(candidate)
        
print "first method (brutforce): sum: ", sum(primes[:-1])

# Sieve of Eratosthenes

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
    sum += curr
print "second method (sieve of Eratosthenes): sum: ", sum


print sieve[0:20]
