""" 
6.4 
Из заданной строки получить список слов, у которых третья с конца буква согласная, а предпоследняя – гласная.
"""
import re

text = list(input('Введите строку для поиска по ней: ').split())

sort_lst = []

for word in text:
    if re.findall(r'[бвгдзжкйлмнпрстфхцчшщьъ][аеиоуыэюя]\w\b', word):
        sort_lst.append(word)

print("Вот в каких словах найден требуеммый паттерн: ")
for word in sort_lst:
    print(word)

 
