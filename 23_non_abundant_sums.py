#!/usr/bin/python

# A perfect number is a number for which the sum of its proper divisors is exactly
# equal to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.

# Find the sum of all the positive integers which cannot be written as the sum of
# two abundant numbers.


# limit = 28123
# limit = 100
limit = 30000

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
def get_sum_of_divizors(num, primes):
    factors = []
    sum = 1
    original = num
    for prime in primes:
        if num % prime == 0:
            p = prime
            while num % prime == 0:
                p = p * prime
                num /= prime
            sum *= (p - 1) / (prime - 1)
    return sum - original
        

primes = []
precompute_primes(limit, primes)

abandunts = []
for i in xrange(2, limit + 1):
    j = get_sum_of_divizors(i, primes)
    if j > i:
        abandunts.append(i)

abandunts_set = set(abandunts)
print "abandunt numbers:", abandunts_set

non_sum_abandunt = []
for num in xrange(1, limit + 1):
    for j in abandunts:
        if num - j in abandunts_set:
            break
    else:
        non_sum_abandunt.append(num)

print "found numbers that cannot be expressed as sum of 2 abandunt numbers:", non_sum_abandunt, "sum:", sum(non_sum_abandunt)

