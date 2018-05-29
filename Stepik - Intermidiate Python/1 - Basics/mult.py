#! python3
# -*- coding: utf-8 -*-

n, k = map(int, input().split())

def mult(n,k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return mult(n-1, k) + mult(n-1, k-1)
    
print(mult(n,k))