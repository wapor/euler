#!/usr/bin/python

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

triangles = {}
maxp = 1000
for n in range(1, 14):
    for m in range(n + 1, maxp / 2):    
        a = m*m - n*n
        b = 2*n*m
        c = m*m + n*n
        p = a + b + c
        if p > maxp:
            break
        k = 1
        while k * p < maxp:
            # so dirty :)
            triangles.setdefault(k * p, set()).add(str(sorted((k * a, k * b, k * c))))
            k += 1

maxlen = 0
result = 0
for key, val in sorted(triangles.iteritems()):
    print key, len(val), "->", val
    if len(val) > maxlen:
        print 'new max key:', key
        maxlen = len(val)
        result = key

print 'result:', result
