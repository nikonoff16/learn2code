#! python3
# -*- coding: utf-8 -*-

class ExtendedStack(list):
    def sum(self):
        first = self.pop()
        second = self.pop()
        self.append(first+second)

    def sub(self):
        first = self.pop()
        second = self.pop()
        self.append(first-second)

    def mul(self):
        first = self.pop()
        second = self.pop()
        self.append(first*second)
    def div(self):
        first = self.pop()
        second = self.pop()
        self.append(first//second)
    def append(self):
        self.append()

a = [foo for foo in range(10)]
x = ExtendedStack()
x.append(10)
# x.append(20)

print(x)
x.sum()
print(x)
