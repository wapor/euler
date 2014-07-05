#!/usr/bin/python

# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:

# 1/2= 0.5
# 1/3= 0.(3)
# 1/4= 0.25
# 1/5= 0.2
# 1/6= 0.1(6)
# 1/7= 0.(142857)
# 1/8= 0.125
# 1/9= 0.(1)
# 1/10= 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.


def print_div(num, digits, cycle_len):
    assert digits[0] == 0
    s = ""
    cycle = ""
    if cycle_len > 0:
        for c in digits[-cycle_len:]:
            cycle += chr(ord('0') + c)
        cycle = "(" + cycle + ")"
    for i in digits[1:len(digits) - cycle_len]:
        s += chr(ord('0') + i)
    if cycle_len:
        print "1/%s = 0.%s [with cycle len: %s]" % (num, s + cycle, cycle_len)
    else:
        print "1/%s = 0.%s" % (num, s + cycle)
        

def div_find_cycle(num):
    d = 1
    res = []
    prev_d = []
    while True:
        while num > d:
            d *= 10
            res.append(0)
            prev_d.append(0)
#         print "d:", d, "curr res:", res, "prev_d:", prev_d
        if d in prev_d:
            cycle_len = len(prev_d) - prev_d.index(d)
#             print "found cycle, len:", cycle_len
            print_div(num, res, cycle_len)
            return cycle_len
        res.append(d / num)
        if d % num == 0:
#             print "no cycle"
            print_div(num, res, 0)
            return 0
        prev_d.append(d)
        d %= num
        d *= 10

max_cycle = 0
num = 0
for i in range(2, 1000):
    curr = div_find_cycle(i)
    if curr > max_cycle:
        max_cycle = curr
        num = i
print "result: num:", num, "max_cycle:", max_cycle
    
        
        
