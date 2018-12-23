"""
3.16 
Напишите программу, удваивающую первый элемент списка (путём создания копии), 
если его значение меньше значения второго элемента. 
"""

target_lst = list(input("Введите элементы списка через пробел: ").split())
print(target_lst)
if target_lst[0] < target_lst[1]:
    target_lst.insert(0, target_lst[0])
print(target_lst)