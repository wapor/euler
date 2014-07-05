#!/usr/bin/python
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 * 1 = 192 192 * 2 = 384 192 * 3 = 576 By concatenating each product we get
# the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
# product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
# 5, giving the pandigital, 918273645, which is the concatenated product of 9
# and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?


import itertools

max = 918273645
cset = set(range(1,10))
print cset
for i in itertools.permutations(xrange(1, 9), 3):
    half = i[0] + i[1] * 10 + i[2] * 100 + 9000
    other_half = half * 2
    s = set(str(half) + str(other_half))
    if len(s) == 9 and '0' not in s:
        num = half * 100000 + other_half
        if num > max:
            max = num
print max
