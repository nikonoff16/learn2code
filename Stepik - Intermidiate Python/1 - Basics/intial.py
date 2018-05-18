#! python3
# -*- coding: utf-8 -*-

number = int(input())
if 1 <= number <= 100:

    list = [int(input()) for foo in range(number)]
    x = 0
    for foo in list:
        x += foo
    print(x)
else:
    print('Wrong number')