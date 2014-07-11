#!/usr/bin/python

# You are given the following information, but you may prefer to do some
# research for yourself.

# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century
#   unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

# Stupid and dirty bruteforce
date = [1901, 1, 6]
stop_date = [2000, 12, 31]

days_in_a_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_larger(date1, date2):  # return true if date1 > date2
    return (date1[0] * 10000 + date1[1] * 100 + date1[2] >
            date2[0] * 10000 + date2[1] * 100 + date2[2])

def days(year, month):
    assert month > 0 and month < 13
    if month != 2:  # not Feb
        return days_in_a_month[month]
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return 29
    else: return 28
    
def next_week(date):
    date[2] += 7
    in_a_month = days(date[0], date[1])
    if date[2] > in_a_month:
        date[2] -= in_a_month
        date[1] += 1
        if date[1] > 12:
            date[1] = 1
            date[0] += 1

num_sundays = 0
while True:
    if date[2] == 1:
        num_sundays += 1
        # print "Sunday on 1st: ", num_sundays
        
    # print "Date: ", date[0], "-", date[1], "-", date[2]
    next_week(date)
    if is_larger(date, stop_date):
        break

print 'Answer:', num_sundays
