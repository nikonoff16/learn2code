#! python3
# -*- coding: utf-8 -*-

summ = None
summ_2 = 0
while summ != 0:
    if summ == None:
        summ = 0
    input_now = int(input())
    summ += input_now
    summ_2 += input_now ** 2
print(summ_2)
