#!/usr/bin/python

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

from bisect import bisect_left

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

# Then precompute the the second part of the sum.
def precompute_double_squares(limit, dsquares):
    dsq = 1;
    ind = 1;
    while dsq < limit:
        dsq = 2 * ind * ind
        dsquares.append(dsq)
        ind += 1

# Return true if the element in the sorted list (binary search)
def HasElement(arr, x):
    pos = bisect_left(arr, x, 0, len(arr))
    return pos != len(arr) and arr[pos] == x

limit = 10000
primes = []
dsquares = []
precompute_primes(limit, primes)
precompute_double_squares(limit, dsquares)

print 'Primes:', primes
print 'DSquares:', dsquares

# Iterate on possible candidate.
for i in xrange(1, limit/2):
    x = i * 2 + 1
    if HasElement(primes, x):  # Only composite numbers.
        print 'Ignoring x:', x
        continue
    print 'Checking x:', x
    q = 0
    while dsquares[q] < x:
        if HasElement(primes, x - dsquares[q]):
            print 'Found sum:', x, '=', x - dsquares[q], '+', dsquares[q]
            break
        q += 1
    else:
        print 'Result:', x
        exit()
        
    
