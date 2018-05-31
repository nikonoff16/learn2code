#! python3
# -*- coding: utf-8 -*-

class Buffer:
    def __init__(self):
        # There's an empty list, but in the task guide there mustn't be any argument. 
        self.lst = []
    def add(self, *a):
        # if self.lst not in self:
        #     self.lst = []
        for item in a:
            self.lst.append(item)
            if len(self.lst) == 5:
                theSumm = 0
                for foo in self.lst:
                    theSumm += foo
                print(theSumm)
                self.lst = []
    
    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()