#!/usr/bin/python

import math

def fib(x):
    f1 = 1
    f2 = 1
    for i in xrange(2, x):
        f = f1 + f2
        f1 = f2
        f2 = f
    return f2



f1 = 1
f2 = 1
term = 2
limit = 1000
while math.log10(f2) < limit - 1:
    f = f1 + f2
    f1 = f2
    f2 = f
    term += 1
    print term, f2
print term


