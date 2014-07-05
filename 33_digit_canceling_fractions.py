#!/usr/bin/python

# euclidean GCD
def gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a

aa = 1
bb = 1
# j/i
for i in range(11, 100):
    if i % 10 == 0: continue
    for j in range(11, i):
        if j % 10 == 0: continue
        i1, i2 = divmod(i, 10)
        j1, j2 = divmod(j, 10)

        a, b = 0, 0
        # ab/ac
        if j1 == i1: a, b = j2, i2
        # ab/ca
        if j1 == i2: a, b = j2, i1
        # ba/ac
        if j2 == i1: a, b = j1, i2
        # ba/ca
        if j2 == i2: a, b = j1, i1

        if a > 0 and 1.0 * j / i == 1.0 * a / b:
            print "Found one: ", j, "/", i, "=", a, "/", b
            aa *= a
            bb *= b

g = gcd(aa, bb)
print aa/g, '/', bb/g
