"""
3.10
Напишите программу, определяющую в списке, содержащем списки целых чисел, количество таких списков, содержащих заданное число. 
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

what_number = int(input("Введите целое число, которое желаете найти во вложенных списках: "))

# Эта функциональность включается только в том случае, если не нужна расположенная с 8 по 16 строки

# list_of_numberlists = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11],
#     [2, 4, 6, 8, 10],
#     [1, 3, 5, 7, 9],
# ]
number_count = 0
for lst in list_of_numberlists:
    if what_number in lst:
        number_count += 1
# Контроль правильного представления слова в финальной строке скриптаы
if number_count % 10 == 1:
    word = "списке"
else:
    word = "списках"

print("Число", what_number, "содержится в", number_count, word)


