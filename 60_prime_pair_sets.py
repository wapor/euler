#!/usr/bin/python

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this
# property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.


import primes

primes = primes.Primes(10000)
primes_list = primes.as_list()
remarkable_len_max = 5

def GenereateRemarkables(remarkable):
    curr_len = len(remarkable)
    if curr_len >= remarkable_len_max:
        print 'Answer:', sum(remarkable), remarkable
        exit()
    for p in primes_list:
        if curr_len > 0 and p < remarkable[curr_len - 1]:
            continue
        for r in remarkable:
            if not primes.is_prime(int(str(r) + str(p))):
                break
            if not primes.is_prime(int(str(p) + str(r))):
                break
        else:
            copy = list(remarkable)
            copy.append(p)
            GenereateRemarkables(copy)

GenereateRemarkables([])
