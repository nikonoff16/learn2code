#python3
# -*- coding: utf-8 -*-

'''
Creating a matrix (maybe endless, if someone wants) from divided by space
strings.
'''
amatrix = []
while True:
    item = input()
    if item != 'end' and item != '':
        item = [*item.split()]
        amatrix.append(item)
    else:
        break
'''Translating amatrix array into integer array and Creating an empty one
'''
amatrix = [[int(amatrix[i][j]) for j in range(len(amatrix[i]))] for i in range(len(amatrix))]
# making new empty matrix for summarising numbers
thematrix = [[0 for j in range(len(amatrix[i]))] for i in range(len(amatrix))]

""" Creating iterators"""
Xes = [0, -1]
Yes = [-1, 0]
check = 0 # Trigger to stop outer cycle after 2 times.
while check < 2:
    for foo in range(len(amatrix)): 
        for egg in range(len(amatrix[foo])):
            # print(amatrix[foo][egg]) # testing how it works (in educational purposes)
            for x in range(len(Xes)):
                thematrix[foo][egg] += amatrix[foo + Yes[x]][egg + Xes[x]]

    amatrix.reverse()
    for egg in range(len(amatrix)):
        amatrix[egg].reverse()
    for egg in range(len(thematrix)):
        thematrix[egg].reverse()
    thematrix.reverse()
    check += 1
for row in thematrix:
    print(' '.join([str(elem) for elem in row]))
