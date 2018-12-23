"""
8.24. 
Дан файл f, содержащий различные даты. Каждая дата – это число, месяц и год. Найти:
а) год с наименьшим номером;
б) все весенние даты;
в) самую позднюю дату.

"""

import re

def create_date_file(name, new=False):
    if new:
        answer = input("Эта операция может уничтожить файл с таким же именем. Чтобы подтвердить создание нового файла, введите 'Да': ")
        if answer not in ['да', 'Да', 'ДА']:
            print("Операция не подтверждена, при открытии файла использован режим дозаписи.")
            with open(name, "a") as writefile:
                pass
        else:
            with open(name, "w") as writefile:
                pass
    
    count = input("Введите количество дат: ")
    while type(count) != int:
        try:
            count = int(count)
        except ValueError:
            print("Недопустимое значение!")
            count = input("Введите количество дат: ")

    print("\nОБРАЗЕЦ ВВОДА: 11.02.1999")

    for i in range(count):
        textlookfor=(r"\d{2}.\d{2}.\d{4}")
        message = input("Введите дату " + str(i+1) + ": ")
        while not re.search(textlookfor , message):
            message = input("Неверный формат даты. пожалуйста повторите ввод" + str(i+1) + ": ")
        with open(name, 'a') as writefile:
            writefile.write(message)
            writefile.write("\n")
            

            
        

def find_date_from_file(file, first=True, last=False, spring=False):
    with open(file, 'r') as readfile:

        year_min = 0
        biggest_date = [0, 0, 0]
        anti_autumn = list()  # для хранения весенних дат, и только

        for item in readfile:
            dt = list(int(foo) for foo in item.rstrip().split('.'))

            if first:
                if year_min > dt[2] or year_min == 0:
                    year_min = dt[2]

            if last:
                if biggest_date[2] < dt[2]:
                    biggest_date = dt
                elif biggest_date[2] == dt[2] and biggest_date[1] < dt[1]:
                    biggest_date = dt
                elif biggest_date[2] == dt[2] and biggest_date[1] == dt[1] and biggest_date[0] < dt[0]:
                    biggest_date = dt

            if spring:
                if dt[1] in [3, 4, 5]:
                    anti_autumn.append(dt)
        # print(year_min, biggest_date, anti_autumn)
    if first:
        print("\nНаименьший год в файле -", year_min)
    if last:
        biggest_date = [str(foo) for foo in biggest_date]
        print("\nСамая поздняя дата в файле - ", '.'.join(biggest_date))
    if spring:
        if anti_autumn:
            print("\nВсе весенние даты в файле:")
            for i in anti_autumn:
                i = [str(foo) for foo in i]
                print('\t', '.'.join(i))
        else:
            print("В файле отстутствуют весенние даты.")

    

# create_date_file("gii.txt")
# find_date_from_file("gii.txt", last=True, spring=False)

