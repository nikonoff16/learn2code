"""
8.4
Дано натуральное n. Записать в файл g целые числа b1, ..., bn. 
При i=1,2,...,n значение bi равно: а) i; б) i*i ; в) i!; г) 2i+1; д) 2i+ 3i+1 .
"""
from math import factorial
n = int(input("Введите натуральное число: "))


for egg in range(1, n+1):
    temp_lst = []
    a, b, c, d, e = str(egg), str(egg*egg), str(factorial(egg)), str(2**(egg+1)), str(2**egg + 3**(egg+1))
    temp_lst = [a, b, c, d, e]
    string_of_num = ', '.join(temp_lst)
    with open('pyramid.txt', 'a') as pyr:
        pyr.write(string_of_num)
        pyr.write('\n')
        
