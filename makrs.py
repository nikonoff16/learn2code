#! python3
# -*- coding: utf-8 -*-
marks_line = []
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        line = [line.strip().split(';')]
        marks_line += line
# print(marks_line)
middle_by_hospital = {1: 0, 2: 0, 3: 0}
count = 0
for students in range(len(marks_line)):
    # print('cycle 1 works')
    puple = 0
    for student in range(1,4):
        # print('cycle 2 works')
        middle_by_hospital[student] += int(marks_line[students][student])
        puple += int(marks_line[students][student])
        if student == 3:
            print(puple / 3)
    count += 1
for mark in middle_by_hospital:
    print(middle_by_hospital[mark] / count, end=' ')