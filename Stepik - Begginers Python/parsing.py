#! python3
# -*- coding: utf-8 -*-

word_string = [foo.lower() for foo in input().split()]
# print(word_string)
parsing = {}

for word in word_string:
    if word in parsing:
        parsing[word] += 1
    else:
        parsing[word] = 1

# print(parsing)
for item in parsing:
    print(item, end=' ')
    print(parsing[item])