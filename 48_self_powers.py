#!/usr/bin/python

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


cut = 10000000000

# get num^num cut down to 10 lest significant digits 
def pow_cut(num):
    res = num
    for i in xrange(1, num):
        res = (res * num) % cut
    print 'pow_cut(', num, '):', res
    return res


limit = 1000
sum = 0
for i in xrange(1, limit + 1):
    sum = (sum + pow_cut(i)) % cut

print 'Result:', sum
