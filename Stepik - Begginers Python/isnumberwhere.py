# python3
# -*- coding: utf-8 -*-

lst = [ int(i) for i in input().split()]
x = int(input())
list = ''
count = 0
for foo in lst:
    if x == foo:
        list = list + str(count) + ' '
    count += 1
if len(list) != 0:
    print(list)
else:
    print('Отсутствует')
