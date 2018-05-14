#! /usr/bin/python3
#! python3
# -*- coding: utf-8

def make_cypher(str1, str2):
    your_dict = dict(zip(str1, str2))
    your_antidict = dict(zip(str2, str1))
    return your_dict, your_antidict

enigma, turing = make_cypher(input(), input())
# print(enigma, turing)

my_list = [input(), input()]
# print(my_list)

for string in my_list:
    decode = ''
    for letter in string:
        decode += enigma[letter]
        if len(decode) == len(string):
            print(decode)
    enigma = turing