#!/usr/bin/python

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes
# that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

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

# Accumulated sums.
def precompute_prime_sums(primes, sums):
    sum = 0
    for p in primes:
        sum += p
        sums.append(sum)

limit = 1000000

primes = []
precompute_primes(limit, primes)
primes_set = set(primes)

sums = [0]
precompute_prime_sums(primes, sums)

# Get absolute maximum numbers of terms in the sum first.
ll = 0
for i in sums:
    ll += 1
    if i >= limit: break

# Decrease the number of primes.
while True:
    ll -= 1
    shift = 0
    sum = 0
    # When reached the limit, the sum will only grow, so don't need to go further.
    while sum < limit:
        sum = sums[ll + shift] - sums[shift]
        if sum in primes_set:
            print 'Result:', sum, 'number of primes in the sum:', ll
            exit()
        shift += 1

# max_len = 0
# for p, prime in primes_enumerated:
#     if p % 1000 == 0: print 'Checking prime[', p, 'out of', len(primes), '] = ', prime
#     for s, sum in sums_enumerated:
#         if sum < prime:
#             continue
#         if s > p:
#             break
#         shift = sums_map.get(sum - prime, -1)
#         if shift != -1:
#            if max_len < s - shift:
#                max_len = s - shift
#                print 'Found prime:', prime, 'which is sum of', max_len, 'primes startring with', primes[shift]

# partial_sums = {}
# for ll in xrange(len(sums) - 1, 0, -1):
#     print 'Computing len: ', ll
#     for shift in xrange(0, len(sums) - ll):
#         sum = sums[shift + ll] - sums[shift]
#         partial_sums[sum] = ll
               
        
# for ll in xrange(len(sums) - 1, 0, -1):
#     print 'Checking len: ', ll
#     for shift in xrange(0, len(sums) - ll):
#         sum = sums[shift + ll] - sums[shift]
# #         print 'len:', len(sums), 'll:', ll, 'shift:', shift, 'sum:', sum
#         if sum in primes_set:
#             print 'found prime:', sum, 'which is sum of', ll, 'primes starting from:', primes[shift]
