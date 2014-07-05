#!/usr/bin/python

sum = 0
sum_of_squares = 0
for i in xrange(1, 101):
    sum += i
    sum_of_squares += i * i
square_of_sums = sum * sum
print "sum of squares: ", sum_of_squares
print "square of sums: ", square_of_sums
print "sum: ", sum
print "diff: ", square_of_sums - sum_of_squares
