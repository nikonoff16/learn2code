"""
4.4
Переменные x, y, z – множества. 
Переменной x присвоить множество всех целых чисел от 8 до 22, 
переменной y - множество всех простых чисел от 8 до 22, 
переменной z - множество всех составных чисел из этого же диапазона.
"""

# Блок контроля ввода диапазона значений
try:
    first, second = input("Введите границы диапазона через пробел (по умолчанию - 8 и 22, числа ниже нуля и ноль - недопустимы): ").split()
except ValueError:
    first, second = '', ''

if not first.isnumeric() or not second.isnumeric() or first == '0':
    print("Неверный формат ввода, установлены значения по умолчанию")
    first, second = 8, 22
else:
    first, second = int(first), int(second)

# Находим простые числа в диапазоне от 2 до second по алгоритму "решето Эратосфена"
numbers = list(range(2, second + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, second+1, number):
            numbers[candidate-2] = 0
# Добавляем единицу в список, так как алгоритм не позволяет сразу ее включить в список
numbers.append(1) 

# Ограничиваем список числами, большими или равными first
simple_lst = list()

for num in numbers:   
    if num >= first:
        simple_lst.append(num)
# создаем множество всех чисел диапазона
x_set = set(range(first, second+1))
# создаем множество простых чисел
y_set = set(simple_lst)
# создаем множество составных чисел
z_set = x_set.difference(y_set)

print("Множество х:", x_set)
print("Множество простых чисел у, принадлежащих х:", y_set)
print("Множество составных чисел z, принадлежащих х:", z_set)
        

