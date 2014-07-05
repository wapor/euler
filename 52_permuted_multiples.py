#!/usr/bin/python

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

max_family = 0

def check_family(num):
    global max_family
    numbers = set(str(num))
    for i in xrange(2, 7):
        xnum = i * num
        if set(str(xnum)) == numbers:
            if i > max_family:
                print i, [j * num for j in xrange(1, i + 1)]
                max_family = i
        else:
            return
        

klimit = 7
for k in xrange(2, klimit + 1):
    for num in xrange(10 ** (k - 1), 2 * (10 ** (k - 1))):
        check_family(num)

