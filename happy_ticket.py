#! python3
# -*- coding: utf-8 -*-
# Вводим строковое представление номера билета
ticket_number = input()
# Проверяем номер билета на шестизначность и цифровое значение
if len(ticket_number) != 6:
    print("Неверный формат билета - введите шестизначное число. \n")
# разделяем нашу строку на две равные половины и сравниваем их.
else:
# обрабатываем возможную ошибку неверного формата числа.
    try:
        test = int(ticket_number)
    except ValueError:
        print("Неверный формат билета - введите цифровое значение. \n")
    else:
        first_part = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
        second_part = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
        if first_part == second_part:
            print("Счастливый")
        else:
            print("Обычный")
