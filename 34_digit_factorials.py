#!/usr/bin/python

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Will use stupid brutforce

def get_facts():
    f = 1
    facts = []
    facts.append(f)
    for i in range(1, 10):
        f *= i
        facts.append(f)
    return facts

def get_sum_fact(num, facts):
    s = 0
    while num > 0:
        num, d = divmod(num, 10)
        s += facts[d]
    return s
    
facts = get_facts()
limit = 7 * facts[9]

result = 0
for i in xrange(10, limit):
    if i == get_sum_fact(i, facts):
        result += i
        print i

print 'result:', result
