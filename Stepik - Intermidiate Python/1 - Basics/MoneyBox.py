#! python3
# -*- coding: utf-8 -*-


class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.limit = capacity
    def can_add(self, v):
        if v <= (self.limit - self.count):
            return True
        else:
            return False
    def add (self, v):
        if self.can_add(v) == True:
            self.count += v


# # Решение #20137099

# class MoneyBox:
#     def __init__(self, capacity):
#         self.count_coin = 0
#         self.capacity = capacity

#     def can_add(self, v):
#         return self.count_coin + v <= self.capacity

#     def add(self, v):
#         if self.can_add(v):
#             self.count_coin += v

a = MoneyBox(10)
print(a.count)
print(a.limit)
a.can_add(11)
print(a.can_add(11))
a.add(11)
print(a.count)
