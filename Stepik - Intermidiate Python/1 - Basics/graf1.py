#! python3
# -*- coding: utf-8 -*-

# klasses = {'object': ['A'], 'A': ['B', 'C'], 'B': ['D'], 'C':['D', 'E'], 'D': [], 'E': []}

# # checks = {'A': ['B'], 'B': ['D'], 'C': ['D'], 'D': ['A'], 'D': ['E']}

# checks = ['A B', 'B D', 'C D', 'D A', 'D E']

# klasses = {}
# checks = []

# graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}

graph = {}

''' Я не разобрался, как эта штука работает. Возможно, мне придется переписать всю эту функцию, понять лучше графы
или что-то еще. Пока я пасс'''

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end: 
        # return path
        return 'Yes'
    if not graph.get(start):
        # return None
        return 'No'
    if end in graph[start]:
            return 'Yes'
    for node in graph[start]:
        if end in graph[node]:
            return 'Yes'
        # if node not in path:
        #     newpath = find_path(graph, node, end, path)
        #     if newpath: return 'Yes' #newpath
    return 'No'

# print(find_path(graph, 'A', 'D'))

depth_graph = int(input())
for iteration in range(depth_graph):
    brick = input()
    if ' : ' in brick:
        child, parents = brick.split(' : ')
        if ' ' in parents:
            parents = [foo for foo in parents.split(' ')]
        else:
            parents = [parents]
    else:
        child = brick
        parents = []
    graph[child] = parents
    for parent in parents:
        if parent not in graph:
            graph[parent] = []

# print(graph)

destination = []

paires = int(input())

for foo in range(paires):
    destination.append(input())

# print(destination)

answers = []

for pair in destination:
    parent, child = pair.split()
    answers.append(find_path(graph, child, parent))

for answer in answers:
    print(answer)