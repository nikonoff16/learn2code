#! python3
# -*- coding: utf-8 -*-
"""
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий 
на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то 
на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
"""

number_list = [foo for foo in input().split()]
number_list.append(number_list[0]) 
number_list.reverse()
number_list.append(number_list[1])
number_list.reverse()

#print(number_list)
iter = 1
new_str=[]
for egg in number_list[1:-1]:
    if len(number_list) == 3:
        new_str += [str(int(number_list[iter-1]))]
        break
    new_str += [str(int(number_list[iter-1])+int(number_list[iter+1]))]
    iter += 1

print(' '.join(new_str)) 



