#!/usr/bin/python

# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

import primes        

step = 1
spiral_non_primes = 1
spiral_primes = 0
limit = 1000 * 1000
primes = primes.Primes(50000)

for step in xrange(1, limit):
    side_len = 2 * step + 1
    # a,b,c,d are corners of the spiral rectangle.
    a = side_len * side_len
    b = a - side_len + 1
    c = b - side_len + 1
    d = c - side_len + 1

    spiral_non_primes += 1  # a is always composite - odd square.
    for x in (d, c, b):
        if primes.is_prime(x):
            spiral_primes += 1
        else:
            spiral_non_primes += 1

    ratio = float(spiral_primes) / (spiral_primes + spiral_non_primes)
    if ratio < 0.10:
        break

print side_len
