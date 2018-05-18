#! python3
# -*- coding: utf-8 -*-

def closest_mod_5(x):
    while True:
        if x % 5 == 0:
            return x
        x += 1
print(closest_mod_5(19))

def printab(a, b, *args):
    print('positional argument a ', a)
    print('positional argument b ', b)
    print('additional arguments: ')
    for arg in args:
        print(arg)
printab(10, 20, 30, 40, 50, 60)