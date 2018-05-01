#python3
# -*- coding: utf-8 -*-

'''
Creating a matrix and filling it with numbers of n_square ** 2.
'''

n_square = int(input())
matrix = [[0]* n_square] * n_square
snake = []


# Making the Snake visible
for row in snake:
    print(' '.join([str(elem) for elem in row]))
