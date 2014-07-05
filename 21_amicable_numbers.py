#!/usr/bin/python

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

limit = 10000
primes = []

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

precompute_primes(limit, primes)
print primes


# "factors" is the list of lists of all primes for a number
# "powers" is the temp set of chosen powers of a particular prime
# "divizors" is the result set of all divizors based on factors
def get_divizors(num, factors, powers, divizors):
    i = len(powers)
    if i == len(factors):
        divizor = 1
        for jj in xrange(0, len(powers)):
            divizor *= factors[jj][0] ** powers[jj]
        if divizor != num:
            divizors.append(divizor)
        return 
    for j in xrange(0, len(factors[i]) + 1):
        powers.append(j)
        get_divizors(num, factors, powers, divizors)
        powers.pop()
    
def get_sum_of_divizors(num, primes):
    factors = factorize(i, primes)
    divizors = []
    get_divizors(i, factors, [], divizors)
    print "num:", num, "factors:", factors, "divizors:", divizors, "sum:", sum(divizors)
    return sum(divizors)
    
sum_of_divizors = [0, 1]
for i in xrange(2, limit):
    sum_of_divizors.append(get_sum_of_divizors(i, primes))
print sum_of_divizors

amicable = set()
for i in xrange(2, limit):
    j = sum_of_divizors[i]
    if j >= limit:
        print "sum of divizors for:", i, "is bigger than limit:", j
        continue
    if sum_of_divizors[j] == i and i != j:
        print "found amicable numbers: ", i, j
        amicable.add(i)
        amicable.add(j)
print "amicable:", amicable, "sum:", sum(amicable)
