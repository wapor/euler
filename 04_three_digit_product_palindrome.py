#!/usr/bin/python

half = 999
while half >= 100:
    num = half * 1000 + (half % 10) * 100 + (half / 10 % 10) * 10 + half / 100
#     print "Examining palindrome: ", num
    half -= 1
    for i in xrange(100, 999):
        if num % i == 0:
            j = num / i
            if j >= 100 and j <= 999:
                print "Here we go:", num, "=", i, "*", j
                exit()
    


