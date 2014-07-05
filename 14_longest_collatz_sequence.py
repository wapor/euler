#!/usr/bin/python

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
        print "New max: ", max
    return steps


max_stop_time = 1;
for i in range(1, limit / 2):
    collatz = Collatz(i)
    if collatz > max_stop_time:
        print "New max stop time: ", max_stop_time, "for i: ", i,\
            "(hits:", cache_hits, "misses:", cache_misses, ")"
        max_stop_time = collatz
