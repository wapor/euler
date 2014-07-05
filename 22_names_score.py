#!/usr/bin/python

filename = 'names.txt'
s = sorted(open(filename, 'r').read().replace('"', '').split(','))
print s

num = 1
total = 0
for i in s:
    sum_i = 0
    for j in i:
        sum_i += ord(j) - ord('A') + 1
    total += num * sum_i
    print "i:", i, "sum:", sum_i, "mul", num * sum_i, "total:", total
    num += 1
print "result:", total

