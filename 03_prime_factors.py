#!/usr/bin/python

import math

num = 600851475143

max = math.sqrt(num)
primes = []

candidate = 1
#while candidate < max:
while num > 1:   
    candidate += 1
    for prime in primes:
        if candidate % prime == 0:
            break
    else:
#         print "Adding new prime:", candidate
        primes.append(candidate)
        while num % candidate == 0:
            print "New factor:", candidate
            num = num / candidate
        

