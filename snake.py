#python3
# -*- coding: utf-8 -*-

'''
Creating a matrix and filling it with numbers of n_square ** 2.
'''

n_square = int(input())
matrix = [[0 for egg in range(n_square)] for foo in range(n_square)]
matrix[0][0] = 1
mark = 0
count = 1
# while count <= (n_square**2):
for firstrow in range(n_square):
    matrix[mark][firstrow] = count
    count += 1
    if firstrow == n_square - 1:
        n_square -= 1
        mark = firstrow
        print('First fixed ordinate is ', mark)

for row in range(n_square):
    matrix[row+1][mark] = count
    count += 1
    if row == n_square-1:
        mark = row
        print('Second fixed ordinate is ', mark, 'row value is', row)
        for row in matrix:
            print(' '.join([str(elem) for elem in row]))





# Making the Snake visible
for row in matrix:
    print(' '.join([str(elem) for elem in row]))
