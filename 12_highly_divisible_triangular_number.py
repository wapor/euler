#!/usr/bin/python

import math
num_primes = 10000
limit = 20000

# first, get some primes
def populate_primes(primes, num_primes):
    primes.extend([2, 3])
    candidate = 3
    while len(primes) <= num_primes:
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
    
# Return list of lists of primes for the number "num"
def factorize(num, primes):
    factors = []
    for prime in primes:
        if num % prime == 0:
            ff = []
            while num % prime == 0:
                ff.append(prime)
                num /= prime
            factors.append(ff)
            if num <= 1:
                break
    else:
        exit("Not enough primes for num %d" % num)
    return factors
            
# brutforce
primes = []
populate_primes(primes, num_primes)
print "Got some primes: ", primes

for k in range(2, limit):
    t = k * (k + 1) / 2   # triangle number for k
    factors = factorize(t, primes)
    divizors = 1
    for f in factors:
        divizors *= len(f) + 1
    print "factors for t:", t, " are:", factors, "divizors: ", divizors
    if divizors > 500:
        exit("Found t: %d" % t)
    
# this can be improved since k and k + 1 are co-primes (no common divizors)
# so factorization need to be done only for k and k + 1 (reusing k + 1 for next iteration).
