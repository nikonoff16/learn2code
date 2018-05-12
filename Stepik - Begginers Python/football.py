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


'''
ЧАСТЬ ВТОРАЯ - СОЗДАНИЕ ТАБЛИЦЫ ОТЧЕТНОСТИ И ОБРАБОТКА ДАННЫХ

'''
otchet = {}
for foo in range(len(list_of_matches)):
    first = 1
    second = 3
    for egg in range(0, 3, 2):
        if list_of_matches[foo][egg] not in otchet:
            otchet[list_of_matches[foo][egg]] = [1, 0, 0, 0, 0]
        else:
            otchet[list_of_matches[foo][egg]].insert(0, (otchet[list_of_matches[foo][egg]].pop(0) + 1))
            # continue
            # Эта хер-пойми-что-за конструкция итерирует количество сыграных матчей в уже имеющихся записях
    for egg in range(0, 3, 2):

        score = 0
        if list_of_matches[foo][first] > list_of_matches[foo][second]:
            # число в списке побед итерируется на один, если победа имела место
            otchet[list_of_matches[foo][egg]].insert(1, (otchet[list_of_matches[foo][egg]].pop(1) + 1))
            score = 3
        elif list_of_matches[foo][first] < list_of_matches[foo][second]:
            # число в списке поражений итеритуется на 1, если поражение имело место
            otchet[list_of_matches[foo][egg]].insert(3, (otchet[list_of_matches[foo][egg]].pop(3) + 1))
        elif list_of_matches[foo][first] == list_of_matches[foo][second]:
            # число в списке ничьих итерируется на один, если ничья имела место
            otchet[list_of_matches[foo][egg]].insert(2, (otchet[list_of_matches[foo][egg]].pop(2) + 1))
            score = 1
        otchet[list_of_matches[foo][egg]].insert(4, (otchet[list_of_matches[foo][egg]].pop(4) + score))
        first = 3
        second = 1

'''
ЧАСТЬ ТРЕТЬЯ - ВЫВОД ИНФОРМАЦИИ
Не самая легкая часть проекта из-за неизвестной проблемы - величина второй секции вдруг оказывалась больше, чем размер 
списка в нем, и возникала IndexError. Решил использовать предопределенные численные границы во внутреннем цикле,
и все надалилось.

'''
for item in otchet:
    print(item, end=':')
    for foo in range(0, 5):
        print(otchet[item][foo], end=' ')
    print()