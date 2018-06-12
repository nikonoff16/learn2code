graph = {}
xception_list = []
check_list = []

''' https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

Приняло решение с первого раза, хотя до этого даже не решался браться за него, а задание из темы классов сделал почти
 случайно. Разобраться помогла статья по поиску в графах ﻿, после чего уже осмысленно переписал решение к классам 
 и вот с первого раза сдал эту задачу. До этого не мог сообразить, как правильно ходить по графу, если там множество ветвей.

Первая же ﻿функция из статьи позволяет искать все связанные точки в графе, в зависимости от того, как мы храним данные:

﻿Если у каждой точки храним ее прямых ﻿предков и прямых сыновей, то ﻿
возвращается ﻿все множество ﻿от прадедов до правнуков, независимо от точки вхождения.
Если у точки храним только ﻿прямых предков, то ﻿возвращается множество от точки до прадедов.
Если у точки храним только прямых сыновей, то возвращается множество от точки до ﻿﻿правнуков.
﻿Собственно задача про классы элементарно решается вторым способом, а эта задача так же просто третьим. 
﻿После первого же запроса мы получаем множество ﻿всех сыновей-﻿правнуков ﻿этого исключения, и если следующее исключение ﻿
находится внутри этого множества, то ﻿оно лишнее.

И как у всех задач на этом курсе условие мозговыносящее. Самописные исключения ﻿имеют множественное наследование, 
поэтому ﻿в условии говорится именно про множественное наследование, как и в задаче с классами. ﻿В ответ не надо выводить дубли лишних исключений.

﻿Код от задачи с классами отличается ﻿только тем, ﻿в какую часть словаря мы сохраняем предков, а в какую сыновей. И самую малость проверкой ответа.
'''
depth_graph = int(input())
for iteration in range(depth_graph):
    brick = input()
    if ' : ' in brick:
        child, parents = brick.split(' : ')
    else:
        child = brick
        parents = None
    graph[child] = parents

def check_father(graph, ception, xception_list):
    if graph[ception] in xception_list:
        return ception
    if graph[ception] == None:
        return None
    else:
        next = graph[ception]
        check_father(graph, next, xception_list)

print(graph)

excep = int(input())

for ex in range(excep):
    ception = input()
    if len(xception_list) == 0:
        xception_list += [ception]
    elif check_father(graph, ception, xception_list) != None:
        xception_list += [ception]
        check_list += [ception]
    else:
        xception_list += [ception]


print(graph)
print(xception_list)
print(check_list)