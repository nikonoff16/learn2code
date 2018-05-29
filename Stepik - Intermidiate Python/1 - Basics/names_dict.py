#! python3
# -*- coding: utf-8 -*-

# x={'global' : {'parent' : None, 'vars' : []}
namesp_dict = {'None' : 'global'}
variables = {'global': set()}

def create(namespace, parent):
    global namesp_dict
    global variables
    if parent in namesp_dict.values():
        namesp_dict[parent] = namespace
        variables[namespace] = set()


def add(namespace, var):
    global namesp_dict
    global variables
    if namespace in variables:
        variables[namespace].add(var)

def get(namespace, var):
    global namesp_dict
    global variables
    if var in variables[namespace]:
        return namespace
    elif namespace == 'global':
        return None
    else:
        for key in namesp_dict:
            if namesp_dict[key] == namespace:

                return get(key, var)
    # else:
    #     parent = namesp_dict
    #     return get()

while True:
    count = int(input())
    if count >= 1 or count <= 100:
        break
lst = []
while count > 0:
    cmd, nmsp, var = input().split()
    if cmd == 'get':
        lst.append(get(nmsp, var))
    elif cmd == 'add':
        add(nmsp, var)
    elif cmd == 'create':
        create(nmsp, var)
    count -= 1

for item in lst:
    print(item)

# create('foo', 'global')
# add('foo', 'a')
# add('global', 'b')
print(namesp_dict)
print(variables)
# print(get('foo', 'c'))
# # cmd, nmsp, var = input().split()