#! python3
# -*- coding: utf-8 -*-

def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res

print(s(21))