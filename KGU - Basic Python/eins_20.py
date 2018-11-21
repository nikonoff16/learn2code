'''
Задание 1.20
Определить, можно ли представить число А в виде линейной целочисленной комбинации чисел B и C.
'''

chief_num = int(input("Введите число А: "))
first_slave = int(input("Введите число В: "))
second_slave = int(input("Введите число С: "))

# Использовал алгоритм Евклида для решения задачи

while first_slave != 0 and second_slave != 0:
    if first_slave > second_slave:
        first_slave %= second_slave
        # print(first_slave)
    else:
        second_slave %= first_slave
        # print(second_slave)

res = first_slave + second_slave
print("НОД А и В равен", res)

if chief_num % res == 0:
    print("А можно представить в виде Bx + Cy")
else:
    print("А нельзя представить в виде Bx + Cy")