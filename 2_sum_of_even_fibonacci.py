#!/usr/bin/python

sum = 0
f0 = 0
f1 = 1
f = f0 + f1
while f < 4000000:
    print f
    if f % 2 == 0:
        sum += f
    f0 = f1
    f1 = f
    f = f0 + f1
print "Answer:", sum
    
