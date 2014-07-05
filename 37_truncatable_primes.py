#!/usr/bin/python

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


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

def is_truncatable_prime(num, primes):
    x = 10
    while x < num:
        left, right = divmod(num, x)
        if left not in primes or right not in primes:
            return False
        x *= 10
    return True

limit = 10000000
primes = []
precompute_primes(limit, primes)
set_primes = set(primes)

result = 0
count = 0
for i in primes:
    if i < 10: continue
    if is_truncatable_prime(i, set_primes):
        print i
        result += i
        count += 1
        if count >= 11: break

print 'result:', result

