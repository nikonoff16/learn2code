#! python3
# -*- coding: utf-8 -*-

# x={'global' : {'parent' : None, 'vars' : []}
namesp_dict = {'None' : ['global']}
variables = {'global': set()}

def create(namespace, parent):
    global namesp_dict
    global variables
    if parent in namesp_dict:
        namesp_dict[parent] = namesp_dict.get(parent)
        namesp_dict[parent].append(namespace)
        variables[namespace] = set()
    else:
        check = True
        for foo in namesp_dict:
            for egg in namesp_dict[foo]:
                if egg == parent:
                    namesp_dict[parent] = [namespace]
                    variables[namespace] = set()
                    check = False
                if check == False:
                    break
            if check == False:
                break

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
        for foo in namesp_dict:
            for egg in namesp_dict[foo]:
                if egg == namespace:

                    return get(foo, var)
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