'''
Задание 1.12
Написать программу умножения (деления) двух данных рациональных чисел. Ответ должен быть несократимой дробью.'''

print('''Добро пожаловать! В этой программе Вы можете узнать произведение или отношение двух чисел.
        \nДругие операции не поддерживаются, большее количество чисел ввести также не получится. 
        \nПриятного использования программы! \n''')

the_first_number = float(input("Введите первое число: "))
the_second_number = float(input("Введите второе число: "))
oper = input("Введите желаему операцию (словом без кавычек 'разделить' или 'умножить': ")

while True:
    if oper not in ("разделить", "умножить"):
        oper = input("Допустимое значение оператора только 'разделить' и 'умножить'. Введите корректно название оператора: ")
        continue
    if the_second_number == 0 and oper == "разделить":
        the_second_number = float(input("Деление на ноль не допустимо, введите отличное от нуля число: "))
        continue
    if oper == "разделить":
        print("Результат деления", the_first_number, "на", the_second_number, "равен", the_first_number / the_second_number)
        break
    else:
        print("Результат умножения", the_first_number, "на", the_second_number, "равен", the_first_number / the_second_number)
        break
