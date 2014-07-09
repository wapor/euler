#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

num = 600851475143
primes = []

candidate = 1
largest_factor = 0
while num > 1:   
    candidate += 1
    for prime in primes:
        if candidate % prime == 0:
            break
    else:
        primes.append(candidate)
        while num % candidate == 0:
#             print 'New factor:', candidate
            largest_factor = max(largest_factor, candidate)
            num = num / candidate
        
print 'Answer:', largest_factor
