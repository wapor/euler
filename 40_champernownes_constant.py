#!/usr/bin/python

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

def get_digit(x):
    assert x > 0
    level = 0
    thresh = 0
    print 'x:', x
    while x > thresh:
        start = thresh + 1
        thresh += (level + 1) * 9 * (10 ** (level))
        level += 1
#     print 'level:', level, 'its inclusive start:', start
    y = x - start
    num_idx = y / level
    number = 10 ** (level - 1) + num_idx
    idx = level - 1 - (y - num_idx * level)
#     print 'y:', y, 'num_idx:', num_idx, 'number:', number, 'idx:', idx
    return (number / (10 ** idx)) % 10
    

# sanity check
s = ''
for i in xrange(0,10000):
    s += str(i)

for i in xrange(1,9999):
    assert s[i] == str(get_digit(i))


print 'result:', (get_digit(1) * get_digit(10) * get_digit(100) * get_digit(1000) *
                  get_digit(10000) * get_digit(100000) * get_digit(1000000))
