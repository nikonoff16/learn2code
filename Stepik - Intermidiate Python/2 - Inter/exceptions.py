#! python3
# -*- coding: utf-8 -*-
print('Fuck you')
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    pass
ml = MyList([1, 3, 4])
ml.sort()
try:
    print(ml[4])
except IndexError:
    print('Index Error :(')
print('Fuck you again')