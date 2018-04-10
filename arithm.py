#! python3
# -*- coding: utf-8 -*-

#first, secont = (int(i) for i in input().split())
first = int(input())
secont = int(input())
count = 0
midlle_arithm = 0
if first >= secont:
    print('Fuck you')
elif secont - first < 2:
    print('Fuck you')
else:
    if first % 3 == 2:
        first +=1
    elif first % 3 == 1:
        first +=2
    for foo in range(first, secont + 1, 3):
        midlle_arithm += foo
        count +=1
    print(midlle_arithm / count)
