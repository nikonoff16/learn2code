#! python3
# -*- coding: utf-8 -*-
"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну 
строку значения, которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
"""

number_list = [int(foo) for foo in input().split()]
number_list.sort()
sorted_list = []
for foo in number_list:
    if number_list.index(foo) == 0:   # Если индекс foo равен 0, то:
        sorted_list += [str(foo)]      # Записать значение foo в целевой список
        continue                      # Начать выполнение цикла заново
    elif number_list.count(foo) < 2:
        continue 
    else:
        sorted_list += [str(foo)]


print(' '.join(sorted_list))