#!/usr/bin/python


input1=[
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3],
]

input2=[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

input=input2

assert len(input) > 1
max_path = [[input[0][0]]]
total_max = 0

for j in xrange(1, len(input)):
    paths = []
    print "j:", j, "arr:", input[j]
    
    for i in xrange(0, len(input[j])):
        val_up = input[j][i] + max_path[j - 1][i] if i < j else 0
        val_up_left = input[j][i] + max_path[j - 1][i - 1] if i > 0 else 0
        val = max(val_up, val_up_left)
        paths.append(val)
        total_max = max(val, total_max)
        print "new total_max:", total_max
    max_path.append(paths)
    print "j:", j, "input:", input[j], "paths:", paths
