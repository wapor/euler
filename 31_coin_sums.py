#!/usr/bin/python

currs = [1, 2, 5, 10, 20, 50, 100, 200]

num = 0
def rec(rest, res, m):
    global num
    if rest <= 0:
        num += 1
        return
    use = [i for i in currs if i <= min(m, rest)]
    use.reverse()
    for i in use:
        rec(rest - i, res + [i], i)

res = []
rec(200, res, 200)
print num
