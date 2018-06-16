graph = {}
xception_list = set()
check_list = []

''' https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/ '''

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
    

def dfs1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def check_father(graph, ception, xception_list):
    if ception in xception_list:
        return True
    if len(graph[ception]) == 0:
        return None
    for foo in xception_list:
        if foo == ception: 
            return True
        if foo in dfs1(graph, ception):
            # print(dfs1(graph, ception))
            return True
    return None  

# print(graph)

excep = int(input())

for ex in range(excep):
    ception = input()
    if len(xception_list) == 0:
        xception_list.add(ception)
    elif check_father(graph, ception, xception_list) != None:
        xception_list.add(ception)
        if ception not in check_list:
            check_list += [ception]
    else:
        xception_list.add(ception)

for foo in check_list:
    print(foo)
    

# print(graph)
# print(xception_list)
# print(check_list)
