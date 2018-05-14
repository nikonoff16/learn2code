
#! python3
#! /usr/bin/python3
# -*- coding: utf-8 -*-

height = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0], 11: [0, 0]}
with open('dataset_3380_5.txt') as inf:
    count = 0
    for line in inf:
        line = [foo for foo in line.split()]
        height[int(line[0])][0] += int(line[2])
        height[int(line[0])][1] += 1
        # print(height)

for klass in height:
    if height[klass][1] == 0:
        height[klass] = height[klass][0]
    else:
        height[klass] = height[klass][0] / height[klass][1]
    print(klass, end=' ')
    if height[klass] == 0:
        print('-')
    else:
        print(height[klass])

# print(height)