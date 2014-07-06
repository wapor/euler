#!/usr/bin/python

for b in xrange(1, 1000):
    a = (1000000.0 - 2000 * b) / (2000 - 2 * b)
    if a > 0 and a == int(a):
        c = 1000 - (a + b)
        print "a: ", a, "b: ", b, "c: ", c, "product: ", a * b * c
        
