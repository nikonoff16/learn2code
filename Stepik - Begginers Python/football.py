#! /usr/bin/python3
#! python3
# -*- coding: utf-8

'''
ЧАСТЬ ПЕРВАЯ - ВВОД ДАННЫХ В ПРОГРАММУ
Создаем двумерный массив из данных, удобный для последовательной обработки.

'''
matches_quantity = int(input())
list_of_matches = []
for match in range(matches_quantity):
    list_of_matches += [[foo for foo in input().split(';')]]
# print(list_of_matches)

'''
ЧАСТЬ ВТОРАЯ - СОЗДАНИЕ ТАБЛИЦЫ ОТЧЕТНОСТИ И ОБРАБОТКА ДАННЫХ

'''
otchet = {}
for foo in range(len(list_of_matches)):
    for egg in range(0, 3, 2):
        if list_of_matches[foo][egg] not in otchet:
            otchet[list_of_matches[foo][egg]] = [1]

        else:
            otchet[list_of_matches[foo][egg]].insert(0, (otchet[list_of_matches[foo][egg]].pop(0) + 1))
            # continue
            # Эта хер-пойми-что-за конструкция итерирует количество сыграных матчей в уже имеющихся записях
    # for egg in range(1, 4, 2):
    #     if
# print(otchet)