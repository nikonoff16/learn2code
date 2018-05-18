#! python3
# -*- codning: utf-8 -*-

objects = [1, 2, 1, 2, 3]
ans = 0

fuck = set()
for obj in objects:
    if id(obj) in fuck:
        pass
    else:
        fuck.add(id(obj))
    ans = len(fuck)

print(ans)
