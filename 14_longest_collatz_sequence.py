#!/usr/bin/python

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


limit = 2000000
max = limit
collatz_steps = [0] * limit
collatz_next  = [None] * limit
cache_hits = 0
cache_misses = 0

def Collatz(n):
    "Return stopping time for n in Collatz series. Update dynamic arrays too."
    global max
    global cache_hits
    global cache_misses
    
    if n == 1:
        return 0
    if n < limit and collatz_next[n]:
        cache_hits += 1
        return collatz_steps[n]
    next = (n / 2) if (n % 2 == 0) else (3 * n + 1)
    steps = Collatz(next) + 1
    if n < limit:
        collatz_steps[n] = steps
        collatz_next[n] = next
    else:
        cache_misses += 1
    if n > max:
        max = n
        # print "New max: ", max
    return steps


max_stop_time = 1
max_start = 0
for i in range(1, limit / 2):
    collatz = Collatz(i)
    if collatz > max_stop_time:
        # print "New max stop time: ", max_stop_time, "for i: ", i,\
        #    "(hits:", cache_hits, "misses:", cache_misses, ")"
        max_stop_time, max_start = collatz, i

print 'Answer:', max_start
