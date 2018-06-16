#! python3
# -*- coding: utf-8 -*-


graph = {}


def dfs1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


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
    for foo in parents:
        if foo not in graph:
            graph[foo] = set([])
    graph[child] = set(parents)

# print(graph)

destination = []

paires = int(input())

for foo in range(paires):
    destination.append(input())

# print(destination)

answers = []

for pair in destination:
    parent, child = pair.split()
    if parent == child:
        answers.append('Yes')
    elif parent in dfs1(graph, child):
        answers.append('Yes')
    else:
        answers.append('No')


for answer in answers:
    print(answer)