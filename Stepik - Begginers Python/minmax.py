# python3
# -*- coding: utf-8 -*-

string = [ int(i) for i in input().split()]
m = string[0]
for x in string:
    if m > x:
        m = x
print(m)
