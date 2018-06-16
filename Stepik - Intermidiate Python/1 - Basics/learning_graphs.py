graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

######################################################################
####### CONNECTED COMPONENTS #########################################
def dfs1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(dfs1(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}

###### MORE SUCCINCT RECURSIVE FORM ################################

def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs2(graph, next, visited)
    return visited

print(dfs2(graph, 'C')) # {'E', 'D', 'F', 'A', 'C', 'B'}



'''Вот основная статья по теме. https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
Что не понятно - смотри сюда'''