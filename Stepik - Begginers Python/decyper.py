#! python3
# coding: utf-8 -*-

cyphered_str = ''
decyphered = ''
with open('dataset_3363_2.txt') as inf:
    cyphered_str = inf.read().strip()
''' Этот код классный, и прекрасно работал бы, если бы не было цифр больше 9. Но они есть, и парсинг не получается 
корректным. Нужен другой метод'''
# for cypher in range(0, len(cyphered_str), 2):
#     num = int(cyphered_str[cypher+1])
#     decyphered = decyphered + (cyphered_str[cypher] * num)
#     print(decyphered)
count = 0
while count < len (cyphered_str):
    letter = cyphered_str[count]
    count += 1
    digit = cyphered_str[count]
    count += 1
    if count == len(cyphered_str):
        decyphered += letter * int(digit)
        break
    while True:
        if cyphered_str[count].isdigit() == True:
            digit += cyphered_str[count]
            count += 1
            if count == len(cyphered_str):
                decyphered += letter * int(digit)
                break
        else:
            decyphered += letter * int(digit)
            break
# print(decyphered)
with open('answer.txt', 'w') as ouf:
    ouf.write(decyphered)