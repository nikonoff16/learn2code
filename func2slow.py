#! python3
# -*- coding: utf-8 -*-

def f(x):
    x = 3*x + 1
    return x

cash = {}
count = int(input())
while count > 0:
    x = int(input())
    if x in cash:
        print(cash[x])
        count -= 1
    else:
        cash[x] = f(x)
        print(cash[x])
        count -= 1