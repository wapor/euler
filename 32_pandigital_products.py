#!/usr/bin/python

import itertools

lens = ((1, 4, 4), (2, 3, 4))
# lens = ((1, 2, 0), (2, 1, 0))

digits = [1,2,3,4,5,6,7,8,9]

def is_perm(num, rest):
    while num > 0:
        num, k = divmod(num, 10)
        if k not in rest:
            return False
        else:
            rest.remove(k)
    return len(rest) == 0

def get_num(l):
    num = 0
    for i in l:
        num *= 10
        num += i
    return num

def gen_perm(half1, half2):
    for perm in itertools.permutations(digits, half1 + half2):
        h1 = perm[:half1]
        h2 = perm[half1:]
        rest = set(digits) - set(h1 + h2)
        yield get_num(h1), get_num(h2), rest

result = set()
for trio in lens:
    perm_gen = gen_perm(trio[0], trio[1])
    for l, r, rest in perm_gen:
        num = l * r
        if (is_perm(num, rest)):
            print "Found one:", l, "*", r, "=", num
            result.add(num)

print result, sum(result)
        
        

