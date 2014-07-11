#!/usr/bin/python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

singles = [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]
doubles = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def singles_doubles_str(num):
    assert num < 100 and num > 0
    if num in range(1, 10):
        return singles[num]
    elif num in range(10, 20):
        return teens[num - 10]
    elif num in range(20, 100):
        s = doubles[num / 10]
        if num % 10 != 0:
            s += " " + singles[num % 10]
        return s

def print_num(num):
    if num in range(1, 100):
        return singles_doubles_str(num)
    elif num == 1000:
        return 'one thousand'
    else:
        s = singles[num / 100] + ' hundred'
        if num % 100 != 0:
            s += ' and ' + singles_doubles_str(num % 100)
        return s

limit_inclusive = 1000
str = ''
for i in xrange(1, limit_inclusive + 1):
    print print_num(i)
    str += print_num(i)
print '\nAnswer:', len(str.replace(' ', ''))
