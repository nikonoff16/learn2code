#! python3
# -*- coding: utf-8 -*- 

string = input()
first = input()
second = input()

count = 0

while True:
    if (first == second and first in string):
        print("Impossible")
        break
    if first not in string:
        print(count)
        break
    if first in second:
        print("Impossible")
        break
    
    string = string.replace(first, second)
    count += 1