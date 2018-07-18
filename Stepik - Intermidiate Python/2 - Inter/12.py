import json

starting = json.loads(input())

common = {element['name']: [] for element in starting}

for eli in starting:
    for elc in common:
        if elc in eli['parents']:
            common[elc].append(eli['name'])

for elem in common:
    common[elem] = set(common[elem])

def FUCK(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        FUCK(graph, next, visited)
    return visited

for elem in sorted(common.keys()):
    print(elem, ':', len(FUCK(common, elem)))