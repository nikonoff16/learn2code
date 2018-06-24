#! python3
# -*- coding: utf-8 -*-

from random import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

for x in RandomIterator(10):
    print(x)

def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(15)
print(type(gen))
for i in gen:
    print(i)
# x = RandomIterator(3)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))