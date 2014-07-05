#!/usr/bin/python

fifths = [i**5 for i in range(10)]
print fifths

res = []
limit = 10**6
for i in xrange(10, limit):
    summ = 0
    j = i
    while j > 0:
        summ += fifths[j%10]
        j /= 10
        if summ > i: break
    else:
        if summ == i:
            res.append(i)
            print 'found one:', i
    
print 'result:', sum(res)
