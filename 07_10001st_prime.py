#!/usr/bin/python

import math

primes = [2, 3]

candidate = 3
while len(primes) <= 10001:
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
        print "Adding new prime:", candidate, "total", len(primes)
