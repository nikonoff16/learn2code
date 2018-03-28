#! python3
# -*- coding: utf-8 -*-

coders_count = input()
index = int(coders_count[-1])
length = len(coders_count)
if length > 1:
    index_2 = int(coders_count[-2:])
    print('Index 2 equals ' + str(index_2))
#print('Индекс равен ' + str(index))
#token = int(coders_count)
#print('Токен равен ' + str(token))
#control = 0
#print(index)
#while token > control:
#    if len(coders_count) > 4:
#        print("Программистов очень много, не могу сосчитать корректно.")
#    coders_count = str(coders_count)
if  length >= 2:
    if index_2 == 11 :
        print(coders_count + ' программистов')
    elif index_2 == 12:
        print(coders_count + ' программистов')
    elif index_2 == 13:
        print(coders_count + ' программистов')
    elif index_2 == 14:
        print(coders_count + ' программистов')
    else:
        if index == 1:
            print(coders_count + ' программист')
        elif index == 2:
            print(coders_count + ' программиста')
        elif index == 3:
            print(coders_count + ' программиста')
        elif index == 4:
            print(coders_count + ' программиста')
        else:
            print(coders_count + " программистов")
# if  length == 3:
#     if index_2 == 11 :
#         print(coders_count + ' программистов')
#     elif index_2 == 12:
#         print(coders_count + ' программистов')
#     elif index_2 == 13:
#         print(coders_count + ' программистов')
#     elif index_2 == 14:
#         print(coders_count + ' программистов')
#     else:
#         if index == 1:
#             print(coders_count + ' программист')
#         elif index == 2:
#             print(coders_count + ' программиста')
#         elif index == 3:
#             print(coders_count + ' программиста')
#         elif index == 4:
#             print(coders_count + ' программиста')
#         else:
#             print(coders_count + " программистов")
else:
    if index == 1:
        print(coders_count + ' программист')
    elif index == 2:
        print(coders_count + ' программиста')
    elif index == 3:
        print(coders_count + ' программиста')
    elif index == 4:
        print(coders_count + ' программиста')
    else:
        print(coders_count + " программистов")
# #    coders_count = token
# #    coders_count = str(coders_count)
# #    index = int(coders_count[-1])
