#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

half = 999
while half >= 100:
    num = half * 1000 + (half % 10) * 100 + (half / 10 % 10) * 10 + half / 100
    # print "Examining palindrome: ", num
    half -= 1
    for i in xrange(100, 999):
        if num % i == 0:
            j = num / i
            if j >= 100 and j <= 999:
                print 'Answer:', num, '( =', i, '*', j, ')'
                exit()
    


