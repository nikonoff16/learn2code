#! python3
# -*- coding: utf-8 -*-

count = int(input())
check = 0
number = 1
for foo in range(1, count+1):
    if check >= count:
        break
    for foo in range(1, number+1):
        if check >= count:
            break
        print(number, end=' ')
        check += 1
    number += 1
