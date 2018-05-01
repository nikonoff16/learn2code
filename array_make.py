#python3
# -*- coding: utf-8 -*-

'''
Creating a matrix (maybe endless, if someone wants) from divided by space
strings.
'''
# osX, osY, bomb_count = (int(i) for i in input().split())
amatrix = []
while True:
    item = input()
    if item != 'end' and item != '':
        item = [*item.split()]
        amatrix.append(item)
    else:
        break
amatrix = [[int(amatrix[i][j]) for j in range(len(amatrix[i]))] for i in range(len(amatrix))]
# making new empty matrix for summarising numbers
thematrix = [[0 for j in range(len(amatrix[i]))] for i in range(len(amatrix))]
# print(amatrix)
# print(thematrix)
Xes = [0, 0, 1, -1]
Yes = [1, -1, 0, 0]

for foo in range(len(amatrix)):
    for egg in range(len(amatrix[foo])):
        # print(amatrix[foo][egg]) # testing how it works (in educational purposes)
        for x in range(len(Xes)):
            # if foo == len(amatrix[foo]) or egg ==len(amatrix[foo]) or (foo == len(amatrix[foo]) and egg == len(amatrix[foo])):
            #     thematrix[foo][egg] += amatrix[foo + Yes[x]][egg + Xes[x]]
            print('egg = ', egg, 'len(egg) = ', len(amatrix[egg]), '\n' )
            if foo == len(amatrix[egg]) and x == 2:
                thematrix[foo][egg] += amatrix[foo + Yes[x]][-1 + Xes[x]]
            else:
                thematrix[foo][egg] += amatrix[foo + Yes[x]][egg + Xes[x]]
            print(x, thematrix)
                    # print('foo: ', foo, '  egg: ', egg, '  x: ', x, '  y: ', y)
                    # thematrix[foo][egg] += amatrix[foo + x][egg + y]


print(thematrix)
