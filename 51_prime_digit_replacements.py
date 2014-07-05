#!/usr/bin/python

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated
# numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
# 56993. Consequently 56003, being the first member of this family, is the
# smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import itertools

max_family = 1

# First, get some primes(sieve of Eratosthenes)
def precompute_primes(limit):
    primes = []
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
    return primes

def gen_group_by_indexes(k):
    group_by = []
    for sz in xrange(1, k):  # size of group_by set
        group_by.extend(itertools.combinations(range(k), sz))
    return group_by

def add_to_family(prime, families, group_by):
    global max_family
    lprime = list(str(prime))
    prevx = 'x'
    for ind in group_by:
        if prevx == 'x':
            prevx = lprime[ind]
        if prevx != lprime[ind]:
            return
        lprime[ind] = 'x'

    family = families.setdefault(''.join(lprime), [])
    family.append(prime)
    if len(family) > max_family:
        max_family = len(family)
        print 'group_by', group_by, len(family), ': family[', ''.join(lprime), '] = ', family
    

plimit = 6  # may 5 digit numbers
primes = precompute_primes(10 ** plimit)


for k in xrange(2, plimit + 1):
    group_bys = gen_group_by_indexes(k)
    kprimes = [i for i in primes if i > 10 ** (k-1) and i < 10 ** (k)]
    print 'k:', k, 'primes:', len(kprimes), 'group_bys:', group_bys

    for group_by in group_bys:
        families = {}
        for prime in kprimes:
            add_to_family(prime, families, group_by)
#         print 'group:', group_by, 'families:', families
    
    
    
