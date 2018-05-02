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
for firstrow in range(n_square): #2
    # print(firstrow)
    matrix[mark][firstrow] = count
    count += 1
    if firstrow == n_square - 1:
        n_square -= 1
        mark = firstrow
        print('First fixed ordinate is ', mark)
        break

for row in range(n_square):
    print('secondrow = ', row)
    matrix[row+1][mark] = count
    count += 1
    if row == n_square-1:
        mark = row+1
        print('Second fixed ordinate is ', '\n')
        break
for thirdrow in range(n_square):
    print('thirdrow = ', thirdrow)
    matrix[mark][-(thirdrow)-2] = count
    count += 1
    if thirdrow == n_square-1:
        print('3 = ', thirdrow)
        mark == thirdrow+2
        n_square -= 1
        print('third fixed ordinate is ', mark)
for four in range(n_square):
    print('four = ', four, 'mark = ', mark)
    matrix[(four)-1][mark] = count
    count += 1
    if four == n_square-1:
        mark == thirdrow+1

        print('four fixed ordinate is ', mark)





# Making the Snake visible
for row in matrix:
    print(' '.join([str(elem) for elem in row]))
