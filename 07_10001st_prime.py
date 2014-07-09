#!/usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

primes = [2, 3]
candidate = 3

while True:
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
        if len(primes) == 10001:
            print "Answer:", candidate
            exit()
