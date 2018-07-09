#! python3
# -*- coding: utf-8 -*-

def updated_count(string, item):
    cnt = 0
    while len(string) >= len(item):
        if string.startswith(item):
            cnt +=1
        string = string[1:]
    return cnt

s = input()
t = input()

print(updated_count(s, t))