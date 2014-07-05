#!/usr/bin/python
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 * 7
# 15 = 3 * 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.

# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?


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


# Return list of lists of primes for the number "num"
def factorize_no_dups(num, primes):
    factors = set()
    for prime in primes:
        if num % prime == 0:
            factors.add(prime)
            while num % prime == 0:
                num /= prime
            if num <= 1:
                break
    else:
        exit("Not enough primes for num %d" % num)
    return factors


start = 100000
limit = 999999
max_chain = 4
primes = []

precompute_primes(limit, primes)

chain = 1
prev_factors = set()
for i in xrange(start, limit + 1):
    factors = factorize_no_dups(i, primes)
    if len(factors) == max_chain:
        if len(prev_factors.intersection(factors)) == 0:
            chain += 1
            if chain >= max_chain:
                print 'Result: ', i - 3, '(', i - 2, i - 1, i, ')'
                exit()
        else:
            chain = 1
    else:
        chain = 0
    prev_factors = factors

