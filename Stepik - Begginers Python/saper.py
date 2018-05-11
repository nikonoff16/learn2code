# python3
# -*- coding: utf-8 -*-
'''
I create Saper-like backend algorithm that marks field cell with numbers,
that shows how many bombs touches the cell.
It's followed by https://stepik.org/lesson/3369/step/6?unit=952
I did this script and all comments only for deeper dive in Python
And I want to left some hint in future, if I would forget some of these algorithms.
'''

'''
Creating variables that contains max height and max width and bomb quantity
'''
osX, osY, bomb_count = (int(i) for i in input().split())

'''
Creating an array form osX and osY
'''
area = [[0 for j in range(osY)] for i in range(osX)]

'''
Placing bobs into its places (manually, by user breaked by space)
'''
for bomb in range(bomb_count):
    row, col = (int(foo) - 1 for foo in input().split())
    area[row][col] = -1
'''
Calculating numbers of bobs each cell touches.
'''
for foo in range(osX):
    for egg in range(osY):
        if area[foo][egg] == 0:
            for d_foo in range(-1, 2):
                for d_egg in range(-1, 2):
                    dotX = foo + d_foo
                    dotY = egg + d_egg
                    # (dotX, dotY)
                    # checking cells, trying to avoid some mistakes and excepitons
                    # the cell shall be into the field
                    if 0 <= dotX < osX and 0 <= dotY < osY and area[dotX][dotY] == -1:
                        area[foo][egg] += 1

for dotX in range(osX):
    for dotY in range(osY):
        if area[dotX][dotY] == -1:
            print('*', end='')
        elif area[dotX][dotY] == 0:
            print('.', end='')
        else:
            print(area[dotX][dotY], end='')
    print()
