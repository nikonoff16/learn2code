#! python3
# -*- coding: utf-8 -*-
all_words = {}
with open('dataset_3363_3.txt', 'r') as inf:
    for line in inf:
        line = line.lower().split()
        # print(line)
        for word in line:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1
# print(all_words)
themostfrequentword = {0: 0}
token = 0
for key in all_words:
    # print(themostfrequentword[token])
    if themostfrequentword[token] < all_words.get(key):
        themostfrequentword = {key: all_words.get(key)}
        token = key

for item in themostfrequentword:
    print(item, end=' ')
    print(themostfrequentword[item])