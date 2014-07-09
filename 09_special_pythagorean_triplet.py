#!/usr/bin/python

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


for b in xrange(1, 1000):
    a = (1000000.0 - 2000 * b) / (2000 - 2 * b)
    if a > 0 and a == int(a):
        c = 1000 - (a + b)
        print 'Answer: ', int(a * b * c), '( = ', a, '*', b, '*', c, ')'
        exit()
        
