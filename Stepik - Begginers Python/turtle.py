#! /usr/bin/python3
#! python3
# -*- coding: utf-8

d = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
check = int(input())
while check > 0:
    direct, num = input().split()
    if direct == 'север' or direct == 'восток':
        d[direct] += int(num)
    elif direct == 'юг' or direct == 'запад':
        d[direct] -= int(num)
    check -= 1
print(d['восток'] + d['запад'], end=' ')
print(d['север'] + d['юг'])