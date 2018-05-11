#! python3
# -*- coding: utf-8 -*-
import random
stop = 0
count = 0
while stop == 0:
    skill = random.randint(1, 999999)
    luck = random.randint(1, 999)
    if luck >= skill:
        print("You're lucky")
        stop += 1
    else:
        print("Be a philosopher")
    count += 1
print(count)
