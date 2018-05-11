#! /usr/bin/python3
#! python3
# -*- coding: utf-8 -*-

import requests
'''
Здесь я делаю считывание из файла, чтобы ручками не править ссылку в коде каждый раз. 
Название файла остается тоже самое.
Обрезание символа переноса строки здесь, в принципе и не нужно было бы, если не первый цикл, разделяющий название файла 
и путь к каталогу файлов. Путь на весь скрипт неизменен, а название файла будет извлекаться из последующих 
'''
with open('dataset_3378_3.txt', 'r') as inf:
    path = inf.read()
    path = path.strip('\n')
name = ''

while True:
    if path[-1] == '/':
        name = name[::-1]
        # print(name)
        break
    else:
        name += path[-1]
        path = path[:-1]
        # print(path, name)


while True:
    filename = path + name
    r = requests.get(filename)
    # print(r.url.strip('%0A'))
    name = r.text
    # print(name)
    if r.text[0:2] == 'We':
        break
print(name)