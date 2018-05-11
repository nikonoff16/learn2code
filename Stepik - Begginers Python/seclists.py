#! python3
# -*- coding: utf-8 -*-
"""
Напишите программу, которая принимает на вход список чисел
в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода 
может быть произвольным.
"""

number_list = [(foo) for foo in input().split()]
number_list.sort() 

#print(number_list)
iter = 0
new_str=[]
for egg in number_list:
    if number_list.count(egg) > 1:
        #print('Счетчик текущей операции равен ', number_list.count(egg))
        #print('Итератор равен ', iter)
        if len(new_str) < 1:
            new_str += [number_list[iter]]
        elif number_list[iter] == number_list[iter-1]:
            pass
        else:
            new_str += [number_list[iter]]
        iter += 1
    else:
        iter += 1

print(' '.join(new_str)) 

# number_list.count(egg)
#    elif number_list[iter] != number_list[iter-1]:
#        new_str += [number_list[iter]]