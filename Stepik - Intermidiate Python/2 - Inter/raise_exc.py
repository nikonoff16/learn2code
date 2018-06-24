#! python3
# -*- coding: utf-8 -*-
class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

# print(greet("Victor"))
# print(greet("victor"))

while True:
    try:
        name = input("Please enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break

print("fuck yourself")
#
# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self, x):
#         if x > 0:
#             super().append(x)
#         else:
#             raise NonPositiveError(str(x) + " is not positive")


# fuck = PositiveList()
# fuck.append(5)
# fuck.append(0)