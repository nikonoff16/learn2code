"""
3.34
Дан список из k элементов, каждый из которых является списком из целых чисел. 
Построить список из чисел, каждое из которых встречается в каждом элементе исходного списка.
"""
# Создаем список из ввода пользователя

stroke_count = int(input("Введите количество рядов с цифрами: "))
list_of_numberlists = []

for foo in range(stroke_count):
    numbers_row = input("Введите через пробел числа ряда: ").split()
    numbers_list = []
    for num in numbers_row:
        numbers_list.append(int(num))
    list_of_numberlists.append(numbers_list)

# Эта функциональность включается только в том случае, если не нужна расположенная с 8 по 16 строки
# list_of_numberlists = [[1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9],]

# Общая переменная для обеих реализаций поиска общих элементов
new_list = []

# Вариант 1, реализованный через метод множеств .intersection()

for row in list_of_numberlists:
    if list_of_numberlists.index(row) == 0:
        new_list = set(row)
    else:
        new_list = set(row).intersection(set(new_list))

# Вариант 2, реализованный через обход списков

# for number in list_of_numberlists[0]:
#     check = 0
#     for lst in list_of_numberlists:
#         for foo in lst:
#             if number == foo and foo not in new_list:
#                 check += 1
#                 continue
#     if check == len(list_of_numberlists):
#         new_list.append(number)

# Вывод результатов, общий для версий

if new_list:
    print("Вот список чисел, которые содержатся во всех вложенных списках")
    for num in new_list:
        print(num)
else:
    print('Списки не содержат общего для всех числа')

