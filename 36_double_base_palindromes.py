#!/usr/bin/python

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)


result = 0
limit = 1000 * 1000
for i in xrange(1, limit, 2):
    if not i % 10: continue
    base10 = str(i)
    base2 = format(i, 'b')
#     print base10, 'vs', base10[::-1], 'AND', base2, 'vs', base2[::-1]
    if base10 == base10[::-1] and base2 == base2[::-1]:
        print base10, base2
        result += i
print 'result:', result
    
    
        
