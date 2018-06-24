#! python3
# -*- coding: utf-8 -*-

def primes():
    x = 2
    while True:
        check = 0
        for foo in range(x):
            if foo == 1 or foo == 0:
                continue
            if x % foo == 0:
                check += 1
        if check == 0:
            yield x
        x += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))